# core/debate.py
# 🗣️ Simulates an AI debate based on supporting and opposing evidence

import random

def generate_debate(articles, claim):
    supporting = [a for a in articles if a['sentiment'] > 0.05]
    opposing = [a for a in articles if a['sentiment'] < -0.05]

    print("🔷 PRO (AI Agent 1):")
    for a in random.sample(supporting, min(2, len(supporting))):
        print(f" - According to {a['title']}, it is clear that {claim.lower()}.")

    print("\n🔶 CON (AI Agent 2):")
    for a in random.sample(opposing, min(2, len(opposing))):
        print(f" - However, {a['title']} argues the opposite, suggesting {claim.lower()} is misleading or false.")

    print("\n🤖 Verdict Exchange:")
    if len(supporting) > len(opposing):
        print("PRO: The majority of evidence favors my position.")
        print("CON: Quantity doesn’t equal quality. Let's evaluate credibility more carefully.")
    elif len(opposing) > len(supporting):
        print("CON: Clearly, most reliable articles disagree with the claim.")
        print("PRO: But a few strong sources still support it. Context matters!")
    else:
        print("PRO: Seems like the evidence is mixed.")
        print("CON: Agreed. This may require deeper investigation.")