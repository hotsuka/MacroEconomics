INDICATORS = {
    "monetary_base": {
        "name_jp": "マネタリーベース",
        "name_en": "Monetary Base",
        "db": "MD01",
        "codes": ["MABS1AN11"],
        "frequency": "M",
        "unit": "億円",
    },
    "money_stock_m2": {
        "name_jp": "マネーストック (M2)",
        "name_en": "Money Stock (M2)",
        "db": "MD02",
        "codes": ["MAM1NAM2M2MO"],
        "frequency": "M",
        "unit": "億円",
    },
    "money_stock_m3": {
        "name_jp": "マネーストック (M3)",
        "name_en": "Money Stock (M3)",
        "db": "MD02",
        "codes": ["MAM1NAM3M3MO"],
        "frequency": "M",
        "unit": "億円",
    },
    "cgpi": {
        "name_jp": "企業物価指数 (CGPI)",
        "name_en": "Corporate Goods Price Index",
        "db": "PR01",
        "codes": ["PRCG20_2200000000"],
        "frequency": "M",
        "unit": "2020=100",
    },
    "exchange_rate_usd_jpy": {
        "name_jp": "為替レート (USD/JPY)",
        "name_en": "Exchange Rate (USD/JPY)",
        "db": "FM08",
        "codes": ["FXERM07"],
        "frequency": "M",
        "unit": "円/ドル",
    },
    "call_rate": {
        "name_jp": "コールレート (無担保翌日物)",
        "name_en": "Call Rate (Uncollateralized Overnight)",
        "db": "FM02",
        "codes": ["STRACLUCON"],
        "frequency": "M",
        "unit": "%",
    },
    "basic_discount_rate": {
        "name_jp": "基準割引率・基準貸付利率",
        "name_en": "Basic Discount / Loan Rate",
        "db": "IR01",
        "codes": ["MADR1M"],
        "frequency": "M",
        "unit": "%",
    },
    "tankan_di": {
        "name_jp": "短観 業況判断DI (大企業製造業)",
        "name_en": "Tankan DI (Large Manufacturing)",
        "db": "CO",
        "codes": [
            "TK99F1000601GCQ01000",
            "TK99F2000601GCQ01000",
        ],
        "frequency": "Q",
        "unit": "%ポイント",
    },
    "balance_of_payments": {
        "name_jp": "国際収支 (経常収支)",
        "name_en": "Balance of Payments (Current Account)",
        "db": "BP01",
        "codes": ["BPBP6JYNCB"],
        "frequency": "M",
        "unit": "億円",
    },
}

# --- Price Analysis indicators ---

PRICE_BY_COMMODITY = {
    "foods": {
        "name_jp": "飲食料品",
        "db": "PR01",
        "code": "PRCG20_2200120001",
    },
    "chemicals": {
        "name_jp": "化学製品",
        "db": "PR01",
        "code": "PRCG20_2200520001",
    },
    "petroleum_coal": {
        "name_jp": "石油・石炭製品",
        "db": "PR01",
        "code": "PRCG20_2200620001",
    },
    "iron_steel": {
        "name_jp": "鉄鋼",
        "db": "PR01",
        "code": "PRCG20_2200920001",
    },
    "electronic_components": {
        "name_jp": "電子部品・デバイス",
        "db": "PR01",
        "code": "PRCG20_2201520001",
    },
    "transportation_equip": {
        "name_jp": "輸送用機器",
        "db": "PR01",
        "code": "PRCG20_2201820001",
    },
    "electric_gas_water": {
        "name_jp": "電力・ガス・水道",
        "db": "PR01",
        "code": "PRCG20_2202210001",
    },
    "lumber_wood": {
        "name_jp": "木材・木製品",
        "db": "PR01",
        "code": "PRCG20_2200320001",
    },
    "nonferrous_metals": {
        "name_jp": "非鉄金属",
        "db": "PR01",
        "code": "PRCG20_2201020001",
    },
}

PRICE_EXPORT_IMPORT = {
    "domestic": {
        "name_jp": "国内企業物価 (総合)",
        "db": "PR01",
        "code": "PRCG20_2200000000",
    },
    "export_yen": {
        "name_jp": "輸出物価 (円ベース)",
        "db": "PR01",
        "code": "PRCG20_2400000000",
    },
    "import_yen": {
        "name_jp": "輸入物価 (円ベース)",
        "db": "PR01",
        "code": "PRCG20_2600000000",
    },
    "export_contract": {
        "name_jp": "輸出物価 (契約通貨ベース)",
        "db": "PR01",
        "code": "PRCG20_2300000000",
    },
    "import_contract": {
        "name_jp": "輸入物価 (契約通貨ベース)",
        "db": "PR01",
        "code": "PRCG20_2500000000",
    },
}

PRICE_DEMAND_STAGE = {
    "stage1_all": {
        "name_jp": "Stage 1 (素原材料)",
        "db": "PR04",
        "code": "PRFI20_1I1A00000",
    },
    "stage2_all": {
        "name_jp": "Stage 2 (中間財)",
        "db": "PR04",
        "code": "PRFI20_1I2A00000",
    },
    "stage3_all": {
        "name_jp": "Stage 3 (最終財)",
        "db": "PR04",
        "code": "PRFI20_1I3A00000",
    },
    "stage1_foods": {
        "name_jp": "Stage 1 食料品",
        "db": "PR04",
        "code": "PRFI20_1I1G00100",
    },
    "stage2_foods": {
        "name_jp": "Stage 2 食料品",
        "db": "PR04",
        "code": "PRFI20_1I2G00100",
    },
    "stage3_foods": {
        "name_jp": "Stage 3 食料品",
        "db": "PR04",
        "code": "PRFI20_1I3G00100",
    },
    "stage1_energy": {
        "name_jp": "Stage 1 エネルギー",
        "db": "PR04",
        "code": "PRFI20_1I1G00200",
    },
    "stage2_energy": {
        "name_jp": "Stage 2 エネルギー",
        "db": "PR04",
        "code": "PRFI20_1I2G00200",
    },
    "stage3_energy": {
        "name_jp": "Stage 3 エネルギー",
        "db": "PR04",
        "code": "PRFI20_1I3G00200",
    },
}

PRICE_SERVICES = {
    "services_all": {
        "name_jp": "サービス価格 (総合)",
        "db": "PR02",
        "code": "PRCS20_5200000000",
    },
    "finance_insurance": {
        "name_jp": "金融・保険",
        "db": "PR02",
        "code": "PRCS20_5200010001",
    },
    "real_estate": {
        "name_jp": "不動産",
        "db": "PR02",
        "code": "PRCS20_5200010002",
    },
    "transportation": {
        "name_jp": "運輸・郵便",
        "db": "PR02",
        "code": "PRCS20_5200010003",
    },
    "info_communications": {
        "name_jp": "情報通信",
        "db": "PR02",
        "code": "PRCS20_5200010004",
    },
    "leasing_rental": {
        "name_jp": "リース・レンタル",
        "db": "PR02",
        "code": "PRCS20_5200010005",
    },
    "advertising": {
        "name_jp": "広告",
        "db": "PR02",
        "code": "PRCS20_5200010006",
    },
}
