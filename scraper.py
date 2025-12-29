import requests
from bs4 import BeautifulSoup

def scraper(url):
    headers = {
        "User-Agent": "Mozilla/5.0"             #it makes your request look like it’s coming from a real web browser
    }

    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    h1 = soup.find("h1")
    title = h1.get_text(strip=True) if h1 else ""

    headings = " ".join(                        # it Extracts SEO-important headings
        h.get_text(strip=True)
        for h in soup.find_all(["h2", "h3"])
    )

    paragraphs = " ".join(                  # here it Extracts main content paragraphs
        p.get_text(strip=True)
        for p in soup.find_all("p")
    )

    return {
        "title": title,
        "headings": headings,
        "content": paragraphs
    }
