# factsynth

Give it a claim; it searches the web, scrapes what it finds, scores each source, and prints a report
on what the sources actually say — with an optional PRO/CON summary of the disagreement.

```sh
python main.py --claim "Artificial sweeteners cause cancer" --debate
```

![CLI example](example/example.png)

## Install

```sh
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python -m textblob.download_corpora
```

The two model downloads are separate steps and easy to miss — spaCy and TextBlob both need corpora
that `pip install` does not fetch.

## Usage

| Flag | |
|---|---|
| `--claim` | The statement to investigate (required) |
| `--debate` | Also print a PRO vs CON summary built from the collected sources |

## Pipeline

| Module | |
|---|---|
| `core/claim_handler.py` | Normalises the input claim |
| `core/search.py` | Finds candidate URLs |
| `core/scraper.py` | Pulls article text |
| `core/extractor.py` | spaCy entities + TextBlob sentiment, relevance to the claim |
| `core/credibility.py` | Scores each source |
| `core/synthesizer.py` | Assembles the report and verdict |
| `core/debate.py` | Optional PRO/CON summary |

Credibility scoring is deliberately simple and worth knowing before you trust the ranking: +5 for
being on a hardcoded list of ~11 domains (BBC, Reuters, Nature, WHO, and so on), +2 for a `.edu`,
`.gov` or `.org` suffix, plus a neutrality term that rewards sentiment near zero and a relevance
term. That means an unknown but excellent source scores low, and any `.org` gets a bump regardless
of who runs it.

## The fragile part

`search.py` finds sources by scraping Google's HTML results page. Google does not support this — it
rate-limits, serves consent interstitials, and changes its markup, so the search step is the thing
most likely to return nothing. The code says as much in its own docstring. Pointing it at a real
search API (SerpAPI, Bing, Brave) is the one change that would make this dependable.

## Scope

A pipeline exercise in stringing together search, scraping, NLP and scoring. The verdict it prints
reflects what a handful of scraped pages happen to say, weighted by a hand-written heuristic — treat
it as a reading list with annotations, not a fact check.

## License

MIT — see [LICENSE](LICENSE).
