def final_decision(sms_result: str, url_result: str, rule_risk: str) -> dict:
    if rule_risk == "HIGH" and (
        sms_result == "SMISHING" or url_result == "PHISHING"
    ):
        return {
            "risk": "CRITICAL",
            "action": "BLOCK TRANSACTION"
        }

    if rule_risk == "MEDIUM":
        return {
            "risk": "WARNING",
            "action": "USER VERIFICATION REQUIRED"
        }

    return {
        "risk": "LOW",
        "action": "ALLOW"
    }
