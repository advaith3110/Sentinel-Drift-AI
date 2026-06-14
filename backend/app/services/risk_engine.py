def get_risk_level(score):

    if score >= 90:
        return "Excellent"

    elif score >= 75:
        return "Good"

    elif score >= 50:
        return "Moderate"

    elif score >= 25:
        return "High Risk"

    else:
        return "Critical"


def calculate_risk_score(findings):

    score = 100

    severity_weights = {
        "Critical": 30,
        "High": 20,
        "Medium": 10,
        "Low": 5
    }

    for finding in findings:

        severity = finding.get("severity")

        if severity in severity_weights:
            score -= severity_weights[severity]

    if score < 0:
        score = 0

    return {
        "risk_score": score,
        "risk_level": get_risk_level(score)
    }