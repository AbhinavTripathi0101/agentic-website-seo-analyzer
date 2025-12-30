from typing import TypedDict, Any
from langgraph.graph import StateGraph, END

from scraper import scraper
from advanced_keyword import advanced_keyword
from seo_analyzer import seo_reasoner
from recommendation_agent import recommendation_agent
from planner_agent import planner_agent


class SEOState(TypedDict):
    url: str
    data: dict
    keywords: Any
    issues: str
    recommendations: str
    decision: str


def scraper_node(state: SEOState):
    return {"data": scraper(state["url"])}


def keyword_node(state: SEOState):
    return {
        "keywords": advanced_keyword(
            state["data"]["content"],
            state["data"]["headings"]
        )
    }


def seo_reason_node(state: SEOState):
    return {
        "issues": seo_reasoner(
            state["keywords"],
            state["data"]["content"]
        )
    }


def recommendation_node(state: SEOState):
    return {
        "recommendations": recommendation_agent(
            state["keywords"],
            state["issues"]
        )
    }


def planner_node(state: SEOState):
    decision = planner_agent(state)
    return {"decision": decision}


def route_decision(state: SEOState):
    if state["decision"] == "ANALYZE":
        return "analyze"
    if state["decision"] == "RECOMMEND":
        return "recommend"
    return END


def build_seo_graph():
    graph = StateGraph(SEOState)

    graph.add_node("scrape", scraper_node)
    graph.add_node("keywords", keyword_node)
    graph.add_node("analyze", seo_reason_node)
    graph.add_node("recommend", recommendation_node)
    graph.add_node("planner", planner_node)

    graph.set_entry_point("scrape")

    graph.add_edge("scrape", "keywords")
    graph.add_edge("keywords", "analyze")
    graph.add_edge("analyze", "planner")

    graph.add_conditional_edges(
        "planner",
        route_decision,
        {
            "analyze": "analyze",
            "recommend": "recommend",
            END: END
        }
    )

    graph.add_edge("recommend", END)

    return graph.compile()
