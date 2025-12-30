from langchain_core.messages import HumanMessage
from llm import llm

def planner_agent(state):
    prompt = f"""
You are an SEO decision-making agent.

SEO issues detected:
{state.get("issues")}

Decision rules:
- If ANY actionable SEO issue is present, return RECOMMEND.
- Only return END if the page is already well optimized and no meaningful action is required.
- Do NOT overthink.

Return ONLY one word:
RECOMMEND or END
"""

    decision = llm.invoke([HumanMessage(content=prompt)]).content.strip()
    return decision
