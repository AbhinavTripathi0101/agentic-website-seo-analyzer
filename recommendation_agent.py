from langchain_core.messages import HumanMessage
from llm import llm

def recommendation_agent(keywords, issues):
    prompt = f"""
    Keywords: {keywords}
    Issues: {issues}

    Suggest SEO improvements to increase traffic and visibility.
    """

    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content
