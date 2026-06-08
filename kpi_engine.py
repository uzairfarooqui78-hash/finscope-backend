def calculate_kpis(df):

    return {
        "total_revenue": float(df["revenue"].sum()),
        "total_cost": float(df["cost"].sum()),
        "total_customers": float(df["customers"].sum()),
        "avg_revenue_per_customer": float(df["revenue"].sum() / max(df["customers"].sum(), 1))
    }
