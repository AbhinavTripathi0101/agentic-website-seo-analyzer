from langchain_core.messages import HumanMessage
from llm import llm

def seo_reasoner(keywords, content):
    prompt = f"""
You are an SEO expert.

Analyze the following page data and identify SEO weaknesses.

Keywords (with importance scores):
{keywords}

Content length: {len(content.split())} words

Return a short list of SEO issues in bullet points.
Be concise and practical.
"""

    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content
