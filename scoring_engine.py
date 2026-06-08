
def calculate_scores(kpis):

    margin = kpis["gross_margin"]
    liquidity = kpis["liquidity_ratio"]
    profit = kpis["profit"]

    health = min(100, margin * 1.2 + liquidity * 10)
    risk = max(0, 100 - health)
    opportunity = min(100, (profit / 1000) * 10) if profit else 0
    funding = min(100, liquidity * 20)

    return {
        "health_score": round(health,2),
        "risk_score": round(risk,2),
        "opportunity_score": round(opportunity,2),
        "funding_score": round(funding,2)
    }

def classify(scores):

    h = scores["health_score"]

    if h >= 80:
        return "Excellent"
    elif h >= 60:
        return "Healthy"
    elif h >= 40:
        return "Medium Risk"
    else:
        return "High Risk"

def run_scoring(kpis):
    scores = calculate_scores(kpis)
    status = classify(scores)

    return {"scores": scores, "status": status}
