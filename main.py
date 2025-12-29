from scraper import scraper
from advanced_keyword import advanced_keyword
from seo_analyzer import seo_analyzer
from recommendation_agent import recommendation_agent

URL = "https://en.wikipedia.org/wiki/Mukesh_Ambani"


data = scraper(URL)

keywords = advanced_keyword(
    data["content"],
    data["headings"]
)

issues = seo_analyzer(keywords, data["content"])
recommendations = recommendation_agent(keywords, issues)

print("\n TOP SEO KEYWORDS:\n")
for k, score in keywords:
    print(f"- {k}  → score: {score}")

print("\n SEO ISSUES:\n", issues)
print("\n SEO RECOMMENDATIONS:\n", recommendations)