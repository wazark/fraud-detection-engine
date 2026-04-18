import re

def analyze_message(message: str):
    score = 0
    reasons = []

    # Urgency detection
    if re.search(r"(urgent|immediately|now|asap)", message, re.IGNORECASE):
        score += 30
        reasons.append("Urgency language detected")

    # Suspicious links
    if re.search(r"http[s]?://", message):
        score += 30
        reasons.append("Contains external link")

    # Impersonation patterns
    if re.search(r"(bank|account|verify|suspended)", message, re.IGNORECASE):
        score += 25
        reasons.append("Possible impersonation attempt")

    # Score classification
    if score >= 60:
        level = "High Risk"
    elif score >= 30:
        level = "Suspicious"
    else:
        level = "Safe"

    return {
        "score": score,
        "level": level,
        "reasons": reasons
    }


if __name__ == "__main__":
    test_message = "Your account has been suspended. Click here immediately: http://fake-link.com"
    result = analyze_message(test_message)

    print("Risk Score:", result["score"])
    print("Level:", result["level"])
    print("Reasons:")
    for r in result["reasons"]:
        print("-", r)