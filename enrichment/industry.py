INDUSTRY_SIGNALS = {
    "E-commerce": [
        "online store",
        "shopping cart",
        "checkout",
        "products",
        "ecommerce",
        "e-commerce",
        "shop online",
    ],

    "SaaS": [
        "software platform",
        "cloud platform",
        "saas",
        "subscription",
        "dashboard",
    ],

    "Fintech": [
        "payments",
        "banking",
        "financial",
        "fintech",
        "transactions",
    ],

    "Cybersecurity": [
        "cybersecurity",
        "security platform",
        "threat detection",
        "endpoint security",
        "vulnerability",
    ],

    "Marketing": [
        "digital marketing",
        "marketing platform",
        "advertising",
        "campaigns",
        "seo",
    ],
}


def detect_industry(text):
    text = text.lower()

    scores = {}

    for industry, signals in INDUSTRY_SIGNALS.items():
        score = 0

        for signal in signals:
            if signal in text:
                score += 1

        if score > 0:
            scores[industry] = score

    if not scores:
        return {
            "industry": "Unknown",
            "evidence": []
        }

    industry = max(scores, key=scores.get)

    evidence = [
        signal
        for signal in INDUSTRY_SIGNALS[industry]
        if signal in text
    ]

    return {
        "industry": industry,
        "evidence": evidence
    }