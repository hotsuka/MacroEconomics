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


# --- Detail Analysis indicators ---

METALS_DETAIL = {
    # Sub-categories
    "smelting": {"name_jp": "非鉄金属製錬・精製", "db": "PR01", "code": "PRCG20_2201030001", "level": "sub"},
    "processed": {"name_jp": "非鉄金属加工製品", "db": "PR01", "code": "PRCG20_2201030002", "level": "sub"},
    # Commodity groups
    "g_copper": {"name_jp": "銅", "db": "PR01", "code": "PRCG20_2201040001", "level": "group"},
    "g_lead_zinc": {"name_jp": "鉛・亜鉛", "db": "PR01", "code": "PRCG20_2201040002", "level": "group"},
    "g_aluminum": {"name_jp": "アルミニウム", "db": "PR01", "code": "PRCG20_2201040003", "level": "group"},
    "g_other_bullion": {"name_jp": "その他の非鉄金属地金", "db": "PR01", "code": "PRCG20_2201040004", "level": "group"},
    "g_wire_cable": {"name_jp": "電線・ケーブル", "db": "PR01", "code": "PRCG20_2201040005", "level": "group"},
    "g_drawn_copper": {"name_jp": "伸銅品", "db": "PR01", "code": "PRCG20_2201040006", "level": "group"},
    "g_al_rolled": {"name_jp": "アルミ圧延製品", "db": "PR01", "code": "PRCG20_2201040007", "level": "group"},
    "g_castings": {"name_jp": "非鉄金属素形材", "db": "PR01", "code": "PRCG20_2201040008", "level": "group"},
    "g_other_products": {"name_jp": "その他の非鉄金属製品", "db": "PR01", "code": "PRCG20_2201040009", "level": "group"},
    # Key products
    "p_copper": {"name_jp": "銅", "db": "PR01", "code": "PRCG20_2201050001", "level": "product"},
    "p_lead_solder": {"name_jp": "鉛地金・はんだ", "db": "PR01", "code": "PRCG20_2201050002", "level": "product"},
    "p_al_alloy": {"name_jp": "アルミニウム合金地金", "db": "PR01", "code": "PRCG20_2201050003", "level": "product"},
    "p_gold": {"name_jp": "金地金", "db": "PR01", "code": "PRCG20_2201050004", "level": "product"},
    "p_silver": {"name_jp": "銀地金", "db": "PR01", "code": "PRCG20_2201050005", "level": "product"},
    "p_copper_rod": {"name_jp": "銅荒引線", "db": "PR01", "code": "PRCG20_2201050006", "level": "product"},
    "p_bare_copper": {"name_jp": "銅裸線", "db": "PR01", "code": "PRCG20_2201050007", "level": "product"},
    "p_plastic_copper": {"name_jp": "プラスチック被覆銅線", "db": "PR01", "code": "PRCG20_2201050008", "level": "product"},
    "p_copper_coil": {"name_jp": "銅巻線", "db": "PR01", "code": "PRCG20_2201050009", "level": "product"},
    "p_power_cable": {"name_jp": "電力・通信用ケーブル", "db": "PR01", "code": "PRCG20_2201050010", "level": "product"},
    "p_copper_rolled": {"name_jp": "銅伸銅品", "db": "PR01", "code": "PRCG20_2201050011", "level": "product"},
    "p_brass_rolled": {"name_jp": "黄銅伸銅品", "db": "PR01", "code": "PRCG20_2201050012", "level": "product"},
    "p_al_rolled": {"name_jp": "アルミ圧延製品", "db": "PR01", "code": "PRCG20_2201050013", "level": "product"},
    "p_cu_al_castings": {"name_jp": "銅・アルミ鋳物", "db": "PR01", "code": "PRCG20_2201050014", "level": "product"},
    "p_al_diecast": {"name_jp": "アルミ合金ダイカスト", "db": "PR01", "code": "PRCG20_2201050015", "level": "product"},
    "p_al_forgings": {"name_jp": "アルミニウム鍛造品", "db": "PR01", "code": "PRCG20_2201050016", "level": "product"},
    "p_precious_rolled": {"name_jp": "貴金属展伸材", "db": "PR01", "code": "PRCG20_2201050017", "level": "product"},
}

FOOD_DETAIL = {
    # Sub-categories
    "sub_food": {"name_jp": "食料品", "db": "PR01", "code": "PRCG20_2200130001", "level": "sub"},
    "sub_beverage": {"name_jp": "飲料", "db": "PR01", "code": "PRCG20_2200130002", "level": "sub"},
    "sub_feed": {"name_jp": "飼料・有機質肥料", "db": "PR01", "code": "PRCG20_2200130003", "level": "sub"},
    "sub_tobacco": {"name_jp": "たばこ", "db": "PR01", "code": "PRCG20_2200130004", "level": "sub"},
    # Commodity groups (top 15 most interesting)
    "g_dairy": {"name_jp": "酪農品", "db": "PR01", "code": "PRCG20_2200140001", "level": "group"},
    "g_meat": {"name_jp": "その他の畜産食料品", "db": "PR01", "code": "PRCG20_2200140002", "level": "group"},
    "g_flour": {"name_jp": "製粉", "db": "PR01", "code": "PRCG20_2200140006", "level": "group"},
    "g_noodles": {"name_jp": "めん類", "db": "PR01", "code": "PRCG20_2200140007", "level": "group"},
    "g_bread": {"name_jp": "パン類", "db": "PR01", "code": "PRCG20_2200140008", "level": "group"},
    "g_confectionery": {"name_jp": "菓子類", "db": "PR01", "code": "PRCG20_2200140009", "level": "group"},
    "g_sugar": {"name_jp": "砂糖", "db": "PR01", "code": "PRCG20_2200140011", "level": "group"},
    "g_starch": {"name_jp": "でん粉", "db": "PR01", "code": "PRCG20_2200140012", "level": "group"},
    "g_oils": {"name_jp": "動植物油脂", "db": "PR01", "code": "PRCG20_2200140014", "level": "group"},
    "g_seasoning": {"name_jp": "調味料", "db": "PR01", "code": "PRCG20_2200140015", "level": "group"},
    "g_frozen": {"name_jp": "冷凍調理食品", "db": "PR01", "code": "PRCG20_2200140016", "level": "group"},
    "g_prepared": {"name_jp": "そう菜・すし・弁当", "db": "PR01", "code": "PRCG20_2200140018", "level": "group"},
    "g_tea_coffee": {"name_jp": "茶・コーヒー", "db": "PR01", "code": "PRCG20_2200140024", "level": "group"},
    "g_soft_drinks": {"name_jp": "清涼飲料", "db": "PR01", "code": "PRCG20_2200140025", "level": "group"},
    "g_beer": {"name_jp": "ビール類", "db": "PR01", "code": "PRCG20_2200140021", "level": "group"},
    "g_feed": {"name_jp": "飼料", "db": "PR01", "code": "PRCG20_2200140027", "level": "group"},
    # Key products
    "p_milk": {"name_jp": "処理牛乳", "db": "PR01", "code": "PRCG20_2200150001", "level": "product"},
    "p_butter": {"name_jp": "バター", "db": "PR01", "code": "PRCG20_2200150004", "level": "product"},
    "p_cheese": {"name_jp": "チーズ", "db": "PR01", "code": "PRCG20_2200150005", "level": "product"},
    "p_meat": {"name_jp": "肉製品", "db": "PR01", "code": "PRCG20_2200150009", "level": "product"},
    "p_wheat_flour": {"name_jp": "小麦粉", "db": "PR01", "code": "PRCG20_2200150015", "level": "product"},
    "p_instant_noodle": {"name_jp": "即席めん", "db": "PR01", "code": "PRCG20_2200150016", "level": "product"},
    "p_bread": {"name_jp": "食パン", "db": "PR01", "code": "PRCG20_2200150020", "level": "product"},
    "p_chocolate": {"name_jp": "チョコレート", "db": "PR01", "code": "PRCG20_2200150028", "level": "product"},
    "p_snack": {"name_jp": "スナック菓子", "db": "PR01", "code": "PRCG20_2200150030", "level": "product"},
    "p_sugar": {"name_jp": "砂糖", "db": "PR01", "code": "PRCG20_2200150036", "level": "product"},
    "p_starch": {"name_jp": "でん粉", "db": "PR01", "code": "PRCG20_2200150037", "level": "product"},
    "p_veg_oil": {"name_jp": "植物油脂", "db": "PR01", "code": "PRCG20_2200150040", "level": "product"},
    "p_margarine": {"name_jp": "マーガリン", "db": "PR01", "code": "PRCG20_2200150044", "level": "product"},
    "p_miso": {"name_jp": "みそ", "db": "PR01", "code": "PRCG20_2200150045", "level": "product"},
    "p_soy_sauce": {"name_jp": "しょう油", "db": "PR01", "code": "PRCG20_2200150046", "level": "product"},
    "p_frozen": {"name_jp": "冷凍調理食品", "db": "PR01", "code": "PRCG20_2200150053", "level": "product"},
    "p_bento": {"name_jp": "すし・弁当・おにぎり", "db": "PR01", "code": "PRCG20_2200150056", "level": "product"},
    "p_coffee": {"name_jp": "コーヒー", "db": "PR01", "code": "PRCG20_2200150073", "level": "product"},
    "p_juice": {"name_jp": "ジュース", "db": "PR01", "code": "PRCG20_2200150075", "level": "product"},
    "p_beer": {"name_jp": "ビール", "db": "PR01", "code": "PRCG20_2200150066", "level": "product"},
    "p_feed": {"name_jp": "配合飼料", "db": "PR01", "code": "PRCG20_2200150083", "level": "product"},
}
