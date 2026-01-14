from agents.rule_agent import rule_check
from agents.sms_agent import sms_ml_predict
from agents.url_agent import url_ml_predict

def decide_sms(text: str) -> str:
    rule_flag = rule_check(text)
    ml_flag = sms_ml_predict(text)

    if rule_flag == 1 or ml_flag == 1:
        return "SMISHING"
    return "SAFE"

def decide_url(url: str) -> str:
    rule_flag = rule_check(url)
    ml_flag = url_ml_predict(url)

    if rule_flag == 1 or ml_flag == 1:
        return "PHISHING"
    return "SAFE"
