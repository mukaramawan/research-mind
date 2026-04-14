from langchain.tools import tool
import requests
import os
from dotenv import load_dotenv
from tavily import TavilyClient
from bs4 import BeautifulSoup
from rich import print

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def search_web(query: str) -> str:
    """Search the web for recent and reliable information on a topic. Returns the title, URL and Snippets"""
    response = tavily.search(query, max_results=5)
    results = []
    for r in response['results']:
        results.append(f"title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n")

    return "\n----\n".join(results)

# print(search_web.invoke("List down the recents updates on the war."))

@tool
def scrape_web(url: str) -> str:
    """Scrape the web url and return the clean text content."""
    try:
        response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'html.parser')
        for tag in soup(['script', 'style', 'header', 'footer', 'nav', 'aside']):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    except Exception as e:
        return f"Error scraping the web: {str(e)}"
    
print(scrape_web.invoke("https://www.bbc.com/news/articles/cjr9qrnp821o"))