# core/extractor.py
# 📚 Extracts facts, entities, and sentiment from articles

import spacy
from textblob import TextBlob

nlp = spacy.load("en_core_web_sm")


def extract_facts(articles, claim):
    """
    Extracts structured data from scraped articles:
    - Named entities
    - Sentiment polarity
    - Relevance to claim
    """
    extracted = []
    for article in articles:
        text = article['text'][:3000]  # Truncate to avoid overload
        doc = nlp(text)
        entities = list(set(ent.text for ent in doc.ents if ent.label_ in {"PERSON", "ORG", "GPE", "DATE"}))
        sentiment = TextBlob(text).sentiment.polarity
        relevance = claim.lower() in text.lower()

        extracted.append({
            "url": article['url'],
            "title": article['title'],
            "entities": entities,
            "sentiment": sentiment,
            "relevant": relevance,
            "text": text
        })

    return extracted