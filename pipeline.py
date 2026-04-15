from agents import build_search_agent, build_reader_agent, writer, critic
from rich import print

def run_research_pipeline(topic: str) -> dict:
    search_agent = build_search_agent()
    
    state = {}

    print("\n" + "="*50)
    print(f"Running search agent...")
    print("="*50)

    results = search_agent.invoke({ "messages": [("user", f"Find recent, reliable and relevant information on the topic: {topic}")]})

    state["results"] = results['messages'][-1].content
    print(f"\nSearch results: {state['results']}")

    print("\n" + "="*50)
    print(f"Running reader agent...")
    print("="*50)

    reader_agent = build_reader_agent()
    reader_results = reader_agent.invoke({"messages": [("user", f"""Based on the following search results about the topic, {topic}
    Pick the most relevant URL and scrape for the content. Search results: {state['results'][:1500]}""")]})

    state["scrapped_content"] = reader_results['messages'][-1].content
    print(f"\nReader results: {state['scrapped_content']}")

    print("\n" + "="*50)
    print(f"Writer is drafting the report...")
    print("="*50)

    combined_research = f"Search Results:\n{state['results']}\n\nScrapped Content:\n{state['scrapped_content']}"
    state["report"] = writer.invoke({"topic": topic, "researchGathered": combined_research})
    print(f"\nFinal Report:\n {state['report']}")

    print("\n" + "="*50)
    print(f"Critic is reviewing the report...")
    print("="*50)

    critic_response = critic.invoke({"report": state["report"]})
    state["critic_review"] = critic_response
    print(f"\nCritic's review:\n {state['critic_review']}")

    return state


if __name__ == "__main__":
    topic = input("Enter the research topic: ")
    run_research_pipeline(topic)