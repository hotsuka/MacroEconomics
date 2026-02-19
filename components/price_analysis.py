import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from boj_client.api import fetch_data_by_code
from boj_client.transformers import json_to_dataframe
from boj_client.series_codes import (
    PRICE_BY_COMMODITY,
    PRICE_EXPORT_IMPORT,
    PRICE_DEMAND_STAGE,
    PRICE_SERVICES,
)

COLORS = px.colors.qualitative.Set2 + px.colors.qualitative.Pastel2


def _fetch_price_series(db: str, code: str, start: str, end: str) -> pd.DataFrame:
    raw = fetch_data_by_code(db=db, codes=[code], start_date=start, end_date=end)
    return json_to_dataframe(raw, frequency="M")


def _multi_line_chart(
    series: dict[str, pd.DataFrame], title: str, y_title: str = "指数 (2020=100)"
) -> go.Figure:
    fig = go.Figure()
    for i, (label, df) in enumerate(series.items()):
        if df.empty:
            continue
        fig.add_trace(go.Scatter(
            x=df["date"], y=df["value"],
            mode="lines", name=label,
            line=dict(color=COLORS[i % len(COLORS)], width=2),
        ))
    fig.update_layout(
        title=title,
        xaxis_title="日付", yaxis_title=y_title,
        template="plotly_white", height=480,
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left"),
    )
    return fig


def render_price_analysis(start_date: str, end_date: str):
    st.subheader("物価詳細分析")

    tab1, tab2, tab3, tab4 = st.tabs([
        "財別比較", "輸出入物価", "川上→川下", "サービス物価",
    ])

    # --- Tab 1: Commodity breakdown ---
    with tab1:
        st.markdown("**企業物価指数 (CGPI) - 財の種類別比較** (2020年=100)")
        series = {}
        for meta in PRICE_BY_COMMODITY.values():
            try:
                df = _fetch_price_series(meta["db"], meta["code"], start_date, end_date)
                series[meta["name_jp"]] = df
            except Exception:
                pass

        if series:
            fig = _multi_line_chart(series, "財別 企業物価指数の推移")
            fig.add_hline(y=100, line_dash="dot", line_color="gray",
                          annotation_text="基準値 (100)")
            st.plotly_chart(fig, use_container_width=True)

            # Latest values bar chart
            latest_data = []
            for label, df in series.items():
                if not df.empty:
                    latest_data.append({"財": label, "指数": df.iloc[-1]["value"]})
            if latest_data:
                bar_df = pd.DataFrame(latest_data).sort_values("指数", ascending=True)
                fig_bar = go.Figure(go.Bar(
                    x=bar_df["指数"], y=bar_df["財"], orientation="h",
                    marker_color=[
                        "#e53e3e" if v > 130 else "#d69e2e" if v > 110 else "#38a169"
                        for v in bar_df["指数"]
                    ],
                    text=[f"{v:.1f}" for v in bar_df["指数"]],
                    textposition="outside",
                ))
                fig_bar.update_layout(
                    title="最新値: 財別インフレ度合い",
                    xaxis_title="指数 (2020=100)",
                    template="plotly_white", height=380,
                    xaxis=dict(range=[80, max(bar_df["指数"]) * 1.15]),
                )
                fig_bar.add_vline(x=100, line_dash="dot", line_color="gray")
                st.plotly_chart(fig_bar, use_container_width=True)

    # --- Tab 2: Export / Import ---
    with tab2:
        st.markdown("**国内・輸出・輸入物価の比較** (2020年=100)")
        series = {}
        for meta in PRICE_EXPORT_IMPORT.values():
            try:
                df = _fetch_price_series(meta["db"], meta["code"], start_date, end_date)
                series[meta["name_jp"]] = df
            except Exception:
                pass

        if series:
            # Split: yen basis vs contract currency basis
            yen_series = {k: v for k, v in series.items() if "契約通貨" not in k}
            contract_series = {k: v for k, v in series.items() if "契約通貨" in k or "国内" in k}

            fig1 = _multi_line_chart(yen_series, "円ベースの物価指数比較")
            fig1.add_hline(y=100, line_dash="dot", line_color="gray")
            st.plotly_chart(fig1, use_container_width=True)

            if contract_series:
                fig2 = _multi_line_chart(contract_series, "契約通貨ベース vs 国内物価")
                fig2.add_hline(y=100, line_dash="dot", line_color="gray")
                st.plotly_chart(fig2, use_container_width=True)

            st.info("円ベースと契約通貨ベースの差は為替変動の影響を示します。"
                    "差が大きいほど、円安/円高が輸出入価格に影響していることを意味します。")

    # --- Tab 3: Demand Stage Pipeline ---
    with tab3:
        st.markdown("**需要段階別物価指数 - 川上から川下への価格転嫁** (2020年=100)")

        stage_categories = {
            "総合": ("stage1_all", "stage2_all", "stage3_all"),
            "食料品": ("stage1_foods", "stage2_foods", "stage3_foods"),
            "エネルギー": ("stage1_energy", "stage2_energy", "stage3_energy"),
        }

        for cat_name, (s1_key, s2_key, s3_key) in stage_categories.items():
            series = {}
            for key in (s1_key, s2_key, s3_key):
                meta = PRICE_DEMAND_STAGE[key]
                try:
                    df = _fetch_price_series(meta["db"], meta["code"], start_date, end_date)
                    series[meta["name_jp"]] = df
                except Exception:
                    pass
            if series:
                fig = _multi_line_chart(series, f"需要段階別: {cat_name}")
                fig.add_hline(y=100, line_dash="dot", line_color="gray")
                st.plotly_chart(fig, use_container_width=True)

        st.info("Stage 1 (素原材料) → Stage 2 (中間財) → Stage 3 (最終財) の順に"
                "価格が転嫁されます。Stage間の差が大きいほど、"
                "川上のコスト上昇が川下に十分転嫁されていないことを示します。")

    # --- Tab 4: Services ---
    with tab4:
        st.markdown("**サービス価格指数 (SPPI) - 業種別比較** (2020年=100)")
        series = {}
        for meta in PRICE_SERVICES.values():
            try:
                df = _fetch_price_series(meta["db"], meta["code"], start_date, end_date)
                series[meta["name_jp"]] = df
            except Exception:
                pass

        if series:
            fig = _multi_line_chart(series, "サービス価格指数の推移")
            fig.add_hline(y=100, line_dash="dot", line_color="gray")
            st.plotly_chart(fig, use_container_width=True)

            # Latest values comparison
            latest_data = []
            for label, df in series.items():
                if not df.empty and label != "サービス価格 (総合)":
                    latest_data.append({"業種": label, "指数": df.iloc[-1]["value"]})
            if latest_data:
                bar_df = pd.DataFrame(latest_data).sort_values("指数", ascending=True)
                fig_bar = go.Figure(go.Bar(
                    x=bar_df["指数"], y=bar_df["業種"], orientation="h",
                    marker_color=COLORS[:len(bar_df)],
                    text=[f"{v:.1f}" for v in bar_df["指数"]],
                    textposition="outside",
                ))
                fig_bar.update_layout(
                    title="最新値: 業種別サービス価格",
                    xaxis_title="指数 (2020=100)",
                    template="plotly_white", height=340,
                    xaxis=dict(range=[90, max(bar_df["指数"]) * 1.12]),
                )
                fig_bar.add_vline(x=100, line_dash="dot", line_color="gray")
                st.plotly_chart(fig_bar, use_container_width=True)
