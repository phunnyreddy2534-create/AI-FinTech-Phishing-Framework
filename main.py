from agents.decision_agent import decide_sms, decide_url

def main():
    print("AI-Driven FinTech Phishing Detection System")
    print("1. Check SMS")
    print("2. Check URL")

    choice = input("Enter choice: ")

    if choice == "1":
        sms = input("Enter SMS text: ")
        print("Result:", decide_sms(sms))

    elif choice == "2":
        url = input("Enter URL: ")
        print("Result:", decide_url(url))

    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
