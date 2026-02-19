import pandas as pd


def json_to_dataframe(api_responses: list[dict], frequency: str = "M") -> pd.DataFrame:
    """Convert BOJ API JSON responses to a pandas DataFrame.

    Actual API response structure:
    {
        "STATUS": 200,
        "RESULTSET": [
            {
                "SERIES_CODE": "FXERM07",
                "FREQUENCY": "MONTHLY",
                "VALUES": {
                    "SURVEY_DATES": [202501, 202502, ...],
                    "VALUES": [156.42, 152.03, ...]
                }
            }
        ]
    }
    """
    records = []
    for resp in api_responses:
        for series in resp.get("RESULTSET", []):
            code = series.get("SERIES_CODE", "")
            if not code:
                continue
            values_obj = series.get("VALUES", {})
            dates = values_obj.get("SURVEY_DATES", [])
            values = values_obj.get("VALUES", [])
            freq = series.get("FREQUENCY", "")
            for date_val, val in zip(dates, values):
                records.append({
                    "code": code,
                    "survey_date": date_val,
                    "value": val,
                    "api_frequency": freq,
                })

    df = pd.DataFrame(records)
    if df.empty:
        return df

    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df = df.dropna(subset=["value"])
    df["date"] = df.apply(
        lambda row: _parse_survey_date(row["survey_date"], row["api_frequency"], frequency),
        axis=1,
    )
    df = df.dropna(subset=["date"])
    df = df.sort_values("date").reset_index(drop=True)
    return df


def _parse_survey_date(date_val: int, api_frequency: str, hint_frequency: str) -> pd.Timestamp:
    """Parse integer SURVEY_DATES based on frequency.

    Monthly:    YYYYMM  (e.g., 202501)
    Quarterly:  YYYYQQ  (e.g., 202001 = Q1 2020)
    Daily:      YYYYMMDD (e.g., 20250106)
    """
    try:
        s = str(int(date_val))
        is_quarterly = api_frequency == "QUARTERLY" or hint_frequency == "Q"

        if len(s) == 8:
            # Daily: YYYYMMDD
            return pd.Timestamp(year=int(s[:4]), month=int(s[4:6]), day=int(s[6:8]))
        elif len(s) == 6:
            year = int(s[:4])
            part = int(s[4:6])
            if is_quarterly:
                # Quarterly: last two digits are 01-04
                month = (part - 1) * 3 + 1
            else:
                # Monthly: last two digits are 01-12
                month = part
            return pd.Timestamp(year=year, month=month, day=1)
        elif len(s) == 4:
            return pd.Timestamp(year=int(s), month=1, day=1)
        else:
            return pd.NaT
    except (ValueError, TypeError):
        return pd.NaT
