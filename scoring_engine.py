def run_scoring(kpis):

    score = 0

    if kpis["total_revenue"] > 1000:
        score += 40
    if kpis["total_cost"] < kpis["total_revenue"]:
        score += 30
    if kpis["total_customers"] > 50:
        score += 30

    return {
        "score": score,
        "grade": "A" if score > 80 else "B" if score > 50 else "C"
    }
