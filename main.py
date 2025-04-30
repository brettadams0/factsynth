# factsynth/main.py
# 🧠 Entry point for FactSynth AI Fact Checker & Debate Agent

from core.claim_handler import clean_claim
from core.search import search_sources
from core.scraper import scrape_urls
from core.extractor import extract_facts
from core.credibility import rank_sources
from core.synthesizer import synthesize_report
from core.debate import generate_debate
import argparse


def main():
    parser = argparse.ArgumentParser(description="🧠 FactSynth: AI Fact Checker & Debater")
    parser.add_argument('--claim', type=str, required=True, help='The claim or statement to analyze.')
    parser.add_argument('--debate', action='store_true', help='Generate an AI debate based on findings.')
    args = parser.parse_args()

    print(f"\n📌 Claim: {args.claim}")

    # Step 1: Clean/normalize the claim
    normalized_claim = clean_claim(args.claim)

    # Step 2: Search for supporting and opposing sources
    print("🔍 Searching web sources...")
    urls = search_sources(normalized_claim)

    # Step 3: Scrape and extract content from those sources
    print(f"🌐 {len(urls)} sources found. Scraping...")
    articles = scrape_urls(urls)

    # Step 4: Extract arguments and key entities
    print("📚 Extracting facts and arguments...")
    extracted = extract_facts(articles, normalized_claim)

    # Step 5: Rank source credibility
    ranked = rank_sources(extracted)

    # Step 6: Synthesize structured report
    print("🧠 Synthesizing final report...\n")
    synthesize_report(ranked, normalized_claim)

    # Optional: Simulated AI debate
    if args.debate:
        print("\n🗣️ Running AI debate...\n")
        generate_debate(ranked, normalized_claim)


if __name__ == '__main__':
    main()
