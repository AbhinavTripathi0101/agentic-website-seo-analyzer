# Agentic-inspired SEO Analyzer

An agentic-inspired AI-based SEO(Search Engine Optimization) analysis system that inspects webpage content, extracts semantic keyword signals, identifies SEO weaknesses, and suggests targeted improvements to enhance visibility and content quality.

---

## Features
- Scrapes live webpages using `requests` and `BeautifulSoup`
- Extracts semantic keywords using phrase-based analysis (unigrams, bigrams, trigrams)
- Scores keyword importance instead of relying on raw text frequency
- Detects basic SEO issues such as thin content and weak keyword signals
- Uses an LLM to generate human-like SEO improvement recommendations

---

## Project Structure

llm.py # LLM initialization (Groq)
scraper.py # Web content scraper
advanced_keyword.py # Keyword extraction and scoring logic
seo_analyzer.py # SEO issue detection
recommendation_agent.py # AI-based SEO recommendations
main.py # Orchestrates the agent workflow


---

## How It Works
1. Scrapes webpage content and headings
2. Extracts and scores semantic keywords
3. Analyzes SEO weaknesses
4. Generates improvement suggestions using an LLM

---

## Setup

### 1. Create and activate a virtual environment
```bash
python -m venv venv

venv\Scripts\activate   # Windows
```

### 2  Install dependencies
pip install -r requirements.txt

### 3 Run
python main.py

### Output Image
![Application Output](https://github.com/user-attachments/assets/3586a2a3-8a58-4395-92be-0df5c7c719a7)


