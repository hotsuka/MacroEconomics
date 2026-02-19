import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


def create_time_series_chart(
    df: pd.DataFrame,
    title: str,
    unit: str,
) -> go.Figure:
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["date"],
        y=df["value"],
        mode="lines+markers",
        name=title,
        line=dict(width=2),
        marker=dict(size=4),
    ))
    fig.update_layout(
        title=title,
        xaxis_title="日付",
        yaxis_title=unit,
        template="plotly_white",
        height=400,
        hovermode="x unified",
    )
    return fig


def create_multi_series_chart(
    dataframes: dict[str, pd.DataFrame],
    title: str,
    unit: str,
) -> go.Figure:
    fig = go.Figure()
    colors = px.colors.qualitative.Set2
    for i, (label, df) in enumerate(dataframes.items()):
        fig.add_trace(go.Scatter(
            x=df["date"],
            y=df["value"],
            mode="lines+markers",
            name=label,
            line=dict(color=colors[i % len(colors)], width=2),
        ))
    fig.update_layout(
        title=title,
        xaxis_title="日付",
        yaxis_title=unit,
        template="plotly_white",
        height=400,
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
    )
    return fig
