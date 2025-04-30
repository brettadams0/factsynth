# core/search.py
# 🔍 Searches for relevant URLs based on the input claim

import requests
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
HEADERS = {"User-Agent": USER_AGENT}


def search_sources(claim, max_results=6):
    """
    Performs a basic Google search and returns a list of URLs
    WARNING: This is a workaround method using HTML scraping. Use SerpAPI or Bing API for production.
    """
    query = quote_plus(claim)
    url = f"https://www.google.com/search?q={query}+site:news+OR+site:edu+OR+site:org"
    response = requests.get(url, headers=HEADERS)

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for a in soup.find_all('a'):
        href = a.get('href')
        if href and href.startswith('/url?q='):
            link = href.split('/url?q=')[1].split('&')[0]
            if 'google.com' not in link:
                links.append(link)
        if len(links) >= max_results:
            break

    return links
