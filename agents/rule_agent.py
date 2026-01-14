import re

SUSPICIOUS_KEYWORDS = [
    "verify", "urgent", "account", "bank", "login",
    "otp", "kyc", "password", "click", "confirm"
]

def rule_check(text: str) -> int:
    text = text.lower()
    for word in SUSPICIOUS_KEYWORDS:
        if word in text:
            return 1
    if re.search(r"http[s]?://", text):
        return 1
    return 0
