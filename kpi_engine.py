
def calculate_kpis(df):

    revenue = df["revenue"].sum()
    profit = df["profit"].sum()

    gross_margin = (profit / revenue) * 100 if revenue else 0
    liquidity = df["assets"].sum() / df["liabilities"].sum() if df["liabilities"].sum() else 0

    return {
        "revenue": float(revenue),
        "profit": float(profit),
        "gross_margin": float(gross_margin),
        "liquidity_ratio": float(liquidity)
    }
