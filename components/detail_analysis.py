import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from components.price_analysis import _fetch_price_series, _multi_line_chart
from boj_client.series_codes import METALS_DETAIL, FOOD_DETAIL

COLORS = px.colors.qualitative.Set2 + px.colors.qualitative.Pastel2

# Notable metal products for time-series spotlight
_METALS_SPOTLIGHT = [
    "p_copper", "p_gold", "p_silver", "p_al_alloy",
    "p_lead_solder", "p_copper_rod", "p_brass_rolled", "p_power_cable",
]

# Notable food products for time-series spotlight
_FOOD_SPOTLIGHT = [
    "p_sugar", "p_veg_oil", "p_chocolate", "p_butter",
    "p_wheat_flour", "p_coffee", "p_instant_noodle", "p_bread",
]


def _fetch_by_level(detail_dict: dict, level: str, start: str, end: str) -> dict[str, pd.DataFrame]:
    """Fetch all series matching the given level from a detail dictionary."""
    series: dict[str, pd.DataFrame] = {}
    for key, meta in detail_dict.items():
        if meta["level"] != level:
            continue
        try:
            df = _fetch_price_series(meta["db"], meta["code"], start, end)
            series[meta["name_jp"]] = df
        except Exception:
            pass
    return series


def _ranking_bar(series: dict[str, pd.DataFrame], title: str) -> go.Figure | None:
    """Create a horizontal bar chart of latest values, sorted ascending."""
    latest_data = []
    for label, df in series.items():
        if not df.empty:
            latest_data.append({"品目": label, "指数": df.iloc[-1]["value"]})
    if not latest_data:
        return None

    bar_df = pd.DataFrame(latest_data).sort_values("指数", ascending=True)
    fig = go.Figure(go.Bar(
        x=bar_df["指数"], y=bar_df["品目"], orientation="h",
        marker_color=[
            "#e53e3e" if v > 130 else "#d69e2e" if v > 110 else "#38a169"
            for v in bar_df["指数"]
        ],
        text=[f"{v:.1f}" for v in bar_df["指数"]],
        textposition="outside",
    ))
    fig.update_layout(
        title=title,
        xaxis_title="指数 (2020=100)",
        template="plotly_white",
        height=max(340, len(bar_df) * 28 + 100),
        xaxis=dict(range=[
            min(80, min(bar_df["指数"]) * 0.9),
            max(bar_df["指数"]) * 1.15,
        ]),
    )
    fig.add_vline(x=100, line_dash="dot", line_color="gray")
    return fig


def _spotlight_chart(
    detail_dict: dict, keys: list[str], start: str, end: str, title: str,
) -> go.Figure | None:
    """Fetch and chart a curated list of products for time-series spotlight."""
    series: dict[str, pd.DataFrame] = {}
    for key in keys:
        meta = detail_dict.get(key)
        if meta is None:
            continue
        try:
            df = _fetch_price_series(meta["db"], meta["code"], start, end)
            series[meta["name_jp"]] = df
        except Exception:
            pass
    if not series:
        return None
    fig = _multi_line_chart(series, title)
    fig.add_hline(y=100, line_dash="dot", line_color="gray",
                  annotation_text="基準値 (100)")
    return fig


def _render_sector_tab(
    detail_dict: dict,
    spotlight_keys: list[str],
    sector_name: str,
    start_date: str,
    end_date: str,
):
    """Render the full analysis for one sector (metals or food)."""

    # 1. Sub-category comparison
    st.markdown(f"**{sector_name} - 小類別比較** (2020年=100)")
    sub_series = _fetch_by_level(detail_dict, "sub", start_date, end_date)
    if sub_series:
        fig = _multi_line_chart(sub_series, f"{sector_name}: 小類別の推移")
        fig.add_hline(y=100, line_dash="dot", line_color="gray",
                      annotation_text="基準値 (100)")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("小類別データを取得できませんでした。")

    # 2. Commodity group comparison
    st.markdown(f"**{sector_name} - 商品群別比較** (2020年=100)")
    group_series = _fetch_by_level(detail_dict, "group", start_date, end_date)
    if group_series:
        fig = _multi_line_chart(group_series, f"{sector_name}: 商品群別の推移")
        fig.add_hline(y=100, line_dash="dot", line_color="gray",
                      annotation_text="基準値 (100)")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("商品群別データを取得できませんでした。")

    # 3. Product ranking bar chart
    st.markdown(f"**{sector_name} - 品目別ランキング (最新値)**")
    product_series = _fetch_by_level(detail_dict, "product", start_date, end_date)
    if product_series:
        fig_bar = _ranking_bar(product_series, f"{sector_name}: 品目別インフレ度合い")
        if fig_bar:
            st.plotly_chart(fig_bar, use_container_width=True)
    else:
        st.info("品目別データを取得できませんでした。")

    # 4. Spotlight time-series
    st.markdown(f"**{sector_name} - 注目品目の時系列** (2020年=100)")
    fig_spot = _spotlight_chart(
        detail_dict, spotlight_keys, start_date, end_date,
        f"{sector_name}: 注目品目の推移",
    )
    if fig_spot:
        st.plotly_chart(fig_spot, use_container_width=True)
    else:
        st.info("注目品目データを取得できませんでした。")


def render_detail_analysis(start_date: str, end_date: str):
    st.subheader("品目別詳細分析")

    tab_metals, tab_food = st.tabs(["非鉄金属詳細", "飲食料品詳細"])

    with tab_metals:
        _render_sector_tab(
            METALS_DETAIL, _METALS_SPOTLIGHT,
            "非鉄金属", start_date, end_date,
        )
        st.info(
            "非鉄金属は国際商品市況や為替レートの影響を強く受けます。"
            "製錬・精製 (川上) と加工製品 (川下) の価格差は、"
            "素材メーカーの価格転嫁の度合いを示します。"
        )

    with tab_food:
        _render_sector_tab(
            FOOD_DETAIL, _FOOD_SPOTLIGHT,
            "飲食料品", start_date, end_date,
        )
        st.info(
            "飲食料品は原材料・エネルギー価格、為替、物流コストなど"
            "複合的な要因で変動します。川上の原材料 (小麦粉・砂糖・油脂) から"
            "川下の加工食品 (パン・菓子・冷凍食品) への価格転嫁に注目してください。"
        )
