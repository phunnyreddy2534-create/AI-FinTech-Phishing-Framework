from agents.sms_agent import analyze_sms
from agents.url_agent import analyze_url
from agents.rule_agent import fintech_rule_agent
from agents.decision_agent import final_decision

def run_system(sms: str, url: str):
    sms_result = analyze_sms(sms)
    url_result = analyze_url(url)

    combined_text = f"{sms} {url}"
    rule_risk = fintech_rule_agent(combined_text)

    decision = final_decision(sms_result, url_result, rule_risk)

    print("\n--- AI-Driven FinTech Security Analysis ---")
    print(f"SMS Agent Result : {sms_result}")
    print(f"URL Agent Result : {url_result}")
    print(f"Rule Agent Risk  : {rule_risk}")
    print(f"Final Decision  : {decision}")

if __name__ == "__main__":
    sample_sms = "Urgent! Update your KYC to avoid account suspension"
    sample_url = "http://verify-paypal-account.net"

    run_system(sample_sms, sample_url)
