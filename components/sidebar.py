import datetime

import streamlit as st

from boj_client.series_codes import INDICATORS


def render_sidebar() -> dict:
    st.sidebar.title("設定")

    st.sidebar.subheader("期間選択")
    today = datetime.date.today()

    col1, col2 = st.sidebar.columns(2)
    with col1:
        start_year = st.number_input(
            "開始年", min_value=1990, max_value=today.year, value=2020
        )
        start_month = st.selectbox("開始月", range(1, 13), index=0)
    with col2:
        end_year = st.number_input(
            "終了年", min_value=1990, max_value=today.year, value=today.year
        )
        end_month = st.selectbox("終了月", range(1, 13), index=today.month - 1)

    start_date = f"{start_year}{start_month:02d}"
    end_date = f"{end_year}{end_month:02d}"

    st.sidebar.subheader("表示指標")
    selected = {}
    for key, meta in INDICATORS.items():
        if st.sidebar.checkbox(meta["name_jp"], value=True, key=key):
            selected[key] = meta

    return {
        "start_date": start_date,
        "end_date": end_date,
        "indicators": selected,
    }
