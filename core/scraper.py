# core/scraper.py
# 🌐 Scrapes article content from a list of URLs

import requests
from bs4 import BeautifulSoup

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
HEADERS = {"User-Agent": USER_AGENT}


def scrape_urls(urls):
    """
    Given a list of URLs, return a list of dicts with text content and metadata
    """
    articles = []
    for url in urls:
        try:
            res = requests.get(url, headers=HEADERS, timeout=5)
            soup = BeautifulSoup(res.text, 'html.parser')

            title = soup.title.string.strip() if soup.title else "Untitled"
            paragraphs = soup.find_all('p')
            text = ' '.join(p.get_text().strip() for p in paragraphs)
            if len(text) > 300:
                articles.append({"url": url, "title": title, "text": text})
        except Exception as e:
            print(f"⚠️ Failed to scrape {url}: {e}")

    return articles