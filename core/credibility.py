# core/credibility.py
# 📊 Assigns a credibility score to each source using heuristics

from urllib.parse import urlparse

REPUTABLE_DOMAINS = [
    "bbc.co.uk", "nytimes.com", "harvard.edu", "reuters.com",
    "npr.org", "nature.com", "sciencedaily.com", "history.com",
    "cdc.gov", "who.int", "mit.edu"
]


def rank_sources(extracted_articles):
    """
    Assigns credibility scores to each article based on:
    - Domain authority (hardcoded + suffix-based)
    - Sentiment neutrality (favoring more objective sources)
    - Claim relevance
    """
    ranked = []
    for article in extracted_articles:
        domain = urlparse(article['url']).netloc.replace("www.", "")
        score = 0

        if domain in REPUTABLE_DOMAINS:
            score += 5
        if domain.endswith(".edu") or domain.endswith(".gov") or domain.endswith(".org"):
            score += 2

        neutrality_score = 1 - abs(article['sentiment'])  # closer to 0 is more neutral
        score += neutrality_score * 3

        if article['relevant']:
            score += 2

        article['credibility'] = round(score, 2)
        ranked.append(article)

    return sorted(ranked, key=lambda x: x['credibility'], reverse=True)