# ⚡ Research Mind

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://research-mind-3gsfjpf23yumnksj9mcejr.streamlit.app/)

**Research Mind** is a Multi-Agent Research System that performs deep, automated research on any topic you provide by searching on web and Scraping URls. Using AI agents, it scours the web, compiles comprehensive reports, and provides an objective critique of its own findings—all through a beautifully designed, modern web interface.

🌐 **Live Demo:** [Explore Research Mind](https://research-mind-3gsfjpf23yumnksj9mcejr.streamlit.app/)

## ✨ Features

- **Multi-Agent Architecture:** Utilizes specialized AI agents to handle different stages of the research pipeline (data gathering, report generation, and critiquing).
- **Intelligent Web Scraping:** Employs **BeautifulSoup** to efficiently extract, parse, and clean relevant text content directly from URLs discovered during the research phase.
- **Comprehensive Reports:** Generates detailed, well-structured research reports based on custom prompt.
- **Automated Critique:** Includes an automated critic that reviews the generated report for accuracy, bias, and completeness.
- **Modern UI:** Features a sleek, responsive, and customized Streamlit interface with smooth gradients and typography.
- **Powered by Groq & Tavily:** Uses the blazingly fast Groq API for LLM inference and the Tavily API for highly optimized web search.

## 🚀 How It Works

1. **Enter a Topic:** Simply type in the subject you want to research (e.g., *"solid-state batteries in consumer electronics"*).
2. **Agentic Pipeline:** The system triggers the research pipeline, pulling relevant data from the web using Tavily and scraping target URLs with BeautifulSoup.
3. **Synthesis & Review:** The Groq-powered LLM compiles the data into a readable report and subsequently critiques its own work.
4. **View Results:** Read the final report and the critique side-by-side in distinct tabs.

## 🛠️ Installation & Setup

To run this project locally, follow these steps:

### 1. Clone the repository
```bash
git clone https://github.com/mukaramawan/research-mind.git
cd research-mind
```

### 2. Install dependencies
Ensure you have Python 3.8+ installed. Run the following command to install the required packages:
```bash
pip install -r requirements.txt
```

### 3. Set up Environment Variables
The application requires API keys for Groq and Tavily. Create a `.env` file in the root directory (or export them in your terminal):
```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

### 4. Run the Streamlit App
```bash
streamlit run app.py
```

## 📂 Project Structure

- `app.py`: The main Streamlit application featuring custom CSS and UI logic.
- `pipeline.py`: Orchestrates the multi-agent workflow.
- `agents.py`: Contains the logic and prompts for the individual AI agents (researcher, writer, critic).
- `tools.py`: Helper functions and tools for the agents to interact with external APIs (like Tavily) and scrape web content.
- `requirements.txt`: Python package dependencies.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/mukaramawan/research-mind/issues).
