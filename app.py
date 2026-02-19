import streamlit as st

from config import PAGE_TITLE, PAGE_ICON, PAGE_LAYOUT
from components.sidebar import render_sidebar
from components.charts import create_time_series_chart, create_multi_series_chart
from components.indicators import render_kpi_card
from components.price_analysis import render_price_analysis
from boj_client.api import fetch_data_by_code
from boj_client.transformers import json_to_dataframe

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout=PAGE_LAYOUT)
st.title(PAGE_TITLE)
st.caption("データソース: 日本銀行 時系列統計データ検索サイト API")

selections = render_sidebar()
start_date = selections["start_date"]
end_date = selections["end_date"]
selected_indicators = selections["indicators"]

tab_overview, tab_price = st.tabs(["マクロ概況", "物価詳細分析"])

# === Tab 1: Overview ===
with tab_overview:
    if not selected_indicators:
        st.warning("サイドバーから少なくとも1つの指標を選択してください。")
    else:
        # KPI Summary
        st.subheader("主要指標サマリー")
        kpi_cols = st.columns(min(len(selected_indicators), 4))

        indicator_data = {}
        for i, (key, meta) in enumerate(selected_indicators.items()):
            try:
                raw = fetch_data_by_code(
                    db=meta["db"],
                    codes=meta["codes"],
                    start_date=start_date,
                    end_date=end_date,
                )
                df = json_to_dataframe(raw, frequency=meta["frequency"])
                indicator_data[key] = df
                with kpi_cols[i % len(kpi_cols)]:
                    render_kpi_card(meta["name_jp"], df, meta["unit"])
            except Exception as e:
                indicator_data[key] = None
                with kpi_cols[i % len(kpi_cols)]:
                    st.metric(label=meta["name_jp"], value="エラー")
                    st.caption(str(e)[:100])

        # Charts
        st.subheader("時系列チャート")
        for key, meta in selected_indicators.items():
            df = indicator_data.get(key)
            if df is None or df.empty:
                st.info(f"{meta['name_jp']}: データがありません")
                continue

            if key == "tankan_di" and len(meta["codes"]) > 1:
                dfs = {}
                for code in meta["codes"]:
                    mask = df["code"] == code
                    label = "実績" if "F1" in code else "予測"
                    sub_df = df[mask].copy()
                    if not sub_df.empty:
                        dfs[label] = sub_df
                if dfs:
                    fig = create_multi_series_chart(dfs, meta["name_jp"], meta["unit"])
                else:
                    continue
            else:
                fig = create_time_series_chart(df, meta["name_jp"], meta["unit"])

            st.plotly_chart(fig, use_container_width=True)

            with st.expander(f"{meta['name_jp']} - データテーブル"):
                display_df = df[["date", "value"]].copy()
                display_df.columns = ["日付", f"値 ({meta['unit']})"]
                st.dataframe(display_df, use_container_width=True)

# === Tab 2: Price Analysis ===
with tab_price:
    render_price_analysis(start_date, end_date)
