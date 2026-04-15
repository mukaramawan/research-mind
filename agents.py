from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from tools import search_web, scrape_web

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

def build_search_agent():
    return create_agent(
        model = llm,
        tools=[search_web]
    )

def build_reader_agent():
    return create_agent(
        model = llm,
        tools=[scrape_web]
    )

writer_prompt =  ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful report."),
    ("human", """Write a detail research report on the given topic.
     Topic: {topic}

     Research Gathered: {researchGathered}

     Structure the report as:
     - Introduction
     - Key findings
     - Conclusion
     - Sources

     Report should be in detail, factual and professional.
     """)
])


writer =  writer_prompt | llm | StrOutputParser()

critic_prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic = critic_prompt | llm | StrOutputParser()