import requests
import streamlit as st

from config import API_ENDPOINTS, DEFAULT_FORMAT, DEFAULT_LANG, CACHE_TTL_SECONDS

HEADERS = {
    "Accept-Encoding": "gzip",
    "User-Agent": "MacroEconomics-Dashboard/1.0",
}


@st.cache_data(ttl=CACHE_TTL_SECONDS, show_spinner="日銀APIからデータを取得中...")
def fetch_data_by_code(
    db: str,
    codes: list[str],
    start_date: str | None = None,
    end_date: str | None = None,
    lang: str = DEFAULT_LANG,
    fmt: str = DEFAULT_FORMAT,
) -> list[dict]:
    params = {
        "format": fmt,
        "lang": lang,
        "db": db,
        "code": ",".join(codes),
    }
    if start_date:
        params["startDate"] = start_date
    if end_date:
        params["endDate"] = end_date

    all_data = []
    url = API_ENDPOINTS["data_code"]

    while True:
        response = requests.get(url, params=params, headers=HEADERS, timeout=30)
        response.raise_for_status()
        json_data = response.json()

        status = json_data.get("STATUS")
        if status and str(status) not in ("200", "0"):
            error_msg = json_data.get("ERROR_MSG", "Unknown API error")
            raise RuntimeError(f"BOJ API Error (STATUS={status}): {error_msg}")

        all_data.append(json_data)

        next_pos = json_data.get("NEXTPOSITION")
        if not next_pos:
            break
        params["startPosition"] = next_pos

    return all_data


@st.cache_data(ttl=CACHE_TTL_SECONDS)
def fetch_metadata(db: str, lang: str = DEFAULT_LANG) -> dict:
    params = {"format": "json", "lang": lang, "db": db}
    response = requests.get(
        API_ENDPOINTS["metadata"], params=params, headers=HEADERS, timeout=30
    )
    response.raise_for_status()
    return response.json()
