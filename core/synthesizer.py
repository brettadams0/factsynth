# core/synthesizer.py
# 🧠 Compiles extracted data into a structured Fact vs Fiction report

def synthesize_report(ranked_articles, claim):
    print("📋 FactSynth Report")
    print("=" * 70)
    print(f"Claim: {claim}\n")

    supporting = []
    opposing = []

    for article in ranked_articles:
        sentiment = article['sentiment']
        if sentiment > 0.05:
            supporting.append(article)
        elif sentiment < -0.05:
            opposing.append(article)

    print("🟩 Supporting Evidence:")
    for a in supporting[:3]:
        print(f"- {a['title']} ({a['url']}) [credibility: {a['credibility']}]")

    print("\n🟥 Opposing Evidence:")
    for a in opposing[:3]:
        print(f"- {a['title']} ({a['url']}) [credibility: {a['credibility']}]")

    print("\n⚖️ Summary:")
    if len(supporting) > len(opposing):
        print("The majority of high-credibility sources support this claim.")
    elif len(opposing) > len(supporting):
        print("The majority of high-credibility sources oppose this claim.")
    else:
        print("Evidence is balanced or inconclusive.")

    print("=" * 70)