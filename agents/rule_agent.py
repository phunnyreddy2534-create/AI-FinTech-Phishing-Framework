def fintech_rule_agent(text: str) -> str:
    keywords = [
        "otp", "kyc", "verify", "urgent",
        "account", "bank", "login",
        "password", "card", "upi"
    ]

    score = sum(1 for word in keywords if word in text.lower())

    if score >= 3:
        return "HIGH"
    elif score == 2:
        return "MEDIUM"
    return "LOW"
