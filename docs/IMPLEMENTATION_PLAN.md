# BOJ マクロ経済ダッシュボード 実装計画

## 概要
日本銀行が2026/2/18に公開した時系列統計データ検索サイトのAPI機能を活用し、主要マクロ経済指標をリアルタイムで可視化するStreamlitダッシュボードを構築する。

## 技術スタック
| 技術 | 用途 |
|---|---|
| Python 3.10+ | 実行環境 |
| Streamlit | Webダッシュボードフレームワーク |
| requests | BOJ API HTTP通信 |
| pandas | データ変換・加工 |
| plotly | インタラクティブチャート |

`bojpy`は旧CGIベースのスクレイピング方式であり、2026/2/18公開の新APIに非対応のため使用しない。

## BOJ API仕様

### エンドポイント
- **ベースURL**: `https://www.stat-search.boj.or.jp/api/v1`
- `GET /getDataCode` - 系列コード指定でデータ取得
- `GET /getDataLayer` - 階層情報によるデータ取得
- `GET /getMetadata` - メタデータ取得

### リクエスト形式
```
GET /api/v1/getDataCode?format=json&lang=jp&db={DB}&code={CODE}&startDate={YYYYMM}&endDate={YYYYMM}
```

### 制約
- 1リクエストあたり最大60,000件 / 250系列
- ページネーション: `NEXTPOSITION` フィールド
- 更新頻度: 1日3回 (9:00, 12:00, 15:00 JST)

## 対象マクロ指標

| # | 指標 | DB | CODE | 頻度 | 単位 |
|---|---|---|---|---|---|
| 1 | マネタリーベース | MD01 | MABS1AN11 | 月次 | 億円 |
| 2 | マネーストック M2 | MD02 | MAM1NAM2M2MO | 月次 | 億円 |
| 3 | マネーストック M3 | MD02 | MAM1NAM3M3MO | 月次 | 億円 |
| 4 | 企業物価指数 (CGPI) | PR01 | PRCG20_2200000000 | 月次 | 2020=100 |
| 5 | 為替レート (USD/JPY) | FM08 | FXERM07 | 月次 | 円/ドル |
| 6 | コールレート (無担保翌日物) | FM01 | STRDCLUCON | 月次 | % |
| 7 | 10年国債利回り | IR01 | IRGJBTL10 | 月次 | % |
| 8 | 短観DI (大企業製造業) | CO | TK99F1000601GCQ01000 | 四半期 | %ポイント |
| 9 | 国際収支 (経常収支) | BP01 | BPBP6JYNCB | 月次 | 億円 |

## ファイル構成

```
MacroEconomics/
├── app.py                     # Streamlitメインエントリポイント
├── config.py                  # API URL・キャッシュTTL等の設定
├── requirements.txt           # 依存パッケージ
├── boj_client/
│   ├── __init__.py
│   ├── api.py                 # APIクライアント (fetch + ページネーション + キャッシュ)
│   ├── series_codes.py        # 系列コード定義
│   └── transformers.py        # JSON → pandas DataFrame 変換
├── components/
│   ├── __init__.py
│   ├── sidebar.py             # サイドバー (期間選択・指標選択)
│   ├── charts.py              # Plotlyチャート生成
│   └── indicators.py          # KPIメトリクスカード
├── .streamlit/
│   └── config.toml            # テーマ設定
└── docs/
    └── IMPLEMENTATION_PLAN.md  # 本ファイル
```

## 設計方針

### キャッシュ戦略
- `@st.cache_data(ttl=3600)` で1時間キャッシュ
- BOJの更新サイクル (9:00/12:00/15:00) に合わせた適切なTTL

### エラーハンドリング
- 指標ごとに独立してtry/catch
- 失敗した指標のみエラー表示、他は正常動作継続
- ネットワークタイムアウト: 30秒

### データフロー
```
BOJ API (JSON)
  → boj_client/api.py (fetch + paginate + cache)
  → boj_client/transformers.py (JSON → DataFrame)
  → components/indicators.py (KPIカード)
  → components/charts.py (Plotlyチャート)
  → app.py (Streamlitレイアウト)
```

## 起動方法
```bash
pip install -r requirements.txt
streamlit run app.py
```
