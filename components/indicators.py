import streamlit as st
import pandas as pd


def render_kpi_card(name: str, df: pd.DataFrame, unit: str):
    if df.empty:
        st.metric(label=name, value="データなし")
        return

    latest = df.iloc[-1]
    if len(df) >= 2:
        previous = df.iloc[-2]
        delta = latest["value"] - previous["value"]
        delta_str = f"{delta:+.2f}"
    else:
        delta_str = None

    date_label = latest["date"].strftime("%Y/%m")

    st.metric(
        label=f"{name} ({date_label})",
        value=f"{latest['value']:,.2f} {unit}",
        delta=delta_str,
    )
