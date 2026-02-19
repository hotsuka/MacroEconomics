API_BASE_URL = "https://www.stat-search.boj.or.jp/api/v1"

API_ENDPOINTS = {
    "data_code": f"{API_BASE_URL}/getDataCode",
    "data_layer": f"{API_BASE_URL}/getDataLayer",
    "metadata": f"{API_BASE_URL}/getMetadata",
}

DEFAULT_LANG = "jp"
DEFAULT_FORMAT = "json"
CACHE_TTL_SECONDS = 3600

PAGE_TITLE = "日本銀行 マクロ経済ダッシュボード"
PAGE_ICON = "\U0001f3e6"
PAGE_LAYOUT = "wide"
