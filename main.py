
from agent_graph import build_seo_graph

#URL = "https://en.wikipedia.org/wiki/Mukesh_Ambani"
URL = "https://quotes.toscrape.com/"

app = build_seo_graph()

final_state = app.invoke({"url": URL})

print("\nTOP SEO KEYWORDS:\n")
for k, score in final_state["keywords"]:
    print(f"- {k} → score: {score}")

print("\nSEO ISSUES:\n", final_state["issues"])
print("\nSEO RECOMMENDATIONS:\n", final_state.get("recommendations", "N/A"))
