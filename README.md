# Agentic SEO Analyzer

An agentic AI–based SEO (Search Engine Optimization) analysis system that inspects webpage content, extracts semantic keyword signals, identifies SEO weaknesses, and suggests targeted improvements to enhance content quality and visibility.


## Features
- Scrapes live webpages using `requests` and `BeautifulSoup`
- Extracts semantic keywords using phrase-based analysis (unigrams, bigrams, trigrams)
- Assigns importance scores to keywords instead of relying on raw text frequency
- Uses LLM-based reasoning to identify SEO weaknesses
- Generates human-like SEO improvement recommendations using an LLM
- Implements an agentic workflow using LangGraph with state and decision-based control

---

## Project Structure

llm.py # LLM initialization (Groq)|
scraper.py # Web content scraper|
advanced_keyword.py # Keyword extraction and scoring logic|
seo_reasoner.py # LLM-based SEO issue analysis|
planner_agent.py # Decision-making (recommend or stop)|
recommendation_agent.py # AI-based SEO recommendations|
agent_graph.py # LangGraph-based agent workflow|
main.py # Runs the agentic SEO system

---

## How It Works
1. Scrapes webpage content and headings
2. Extracts and scores semantic keywords
3. Uses LLM-based reasoning to analyze SEO weaknesses
4. A planner agent decides whether recommendations are required
5. Generates SEO improvement suggestions when needed

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
<img width="913" height="884" alt="Agentic SEO Analyzer Output" src="https://github.com/user-attachments/assets/9be142eb-7423-4b02-984c-0905e0c6299f" />



