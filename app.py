import os

import streamlit as st


st.set_page_config(
	page_title="Research Mind",
	page_icon="⚡",
	layout="wide",
	initial_sidebar_state="collapsed",
)


try:
	from pipeline import run_research_pipeline
except Exception as exc:  # pragma: no cover - surfaced in the app UI
	st.error(f"Unable to load the research pipeline: {exc}")
	st.stop()


def inject_styles() -> None:
	st.markdown(
		"""
		<style>
		@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Syne:wght@400;600;700;800&family=Space+Grotesk:wght@500;700&display=swap');



		:root {
			--bg: #f6f9ff;
			--surface: rgba(255, 255, 255, 0.78);
			--border: rgba(15, 23, 42, 0.08);
			--text: #0f172a;
			--muted: #5b667a;
			--accent: #2563eb;
			--accent-2: #06b6d4;
		}

		.stApp {
			background:
				radial-gradient(circle at top left, rgba(37, 99, 235, 0.14), transparent 26%),
				radial-gradient(circle at top right, rgba(6, 182, 212, 0.14), transparent 22%),
				linear-gradient(180deg, #f8fbff 0%, #eef6ff 100%);
			color: var(--text);
			font-family: 'Inter', sans-serif;
		}

		.block-container {
			padding-top: 8rem;
			padding-bottom: 2rem;
			max-width: 1080px;
		}

		.hero {
			padding: 0.15rem 0 1rem 0;
		}

		.eyebrow {
			display: inline-flex;
			align-items: center;
			gap: 0.5rem;
			padding: 0.42rem 0.85rem;
			border-radius: 999px;
			background: rgba(255, 255, 255, 0.72);
			border: 1px solid var(--border);
			color: var(--accent);
			font-size: 0.72rem;
			font-weight: 700;
			letter-spacing: 0.18em;
			text-transform: uppercase;
			box-shadow: 0 10px 30px rgba(15, 23, 42, 0.04);
		}

		.hero h1 {
			margin: 0.85rem 0 0.35rem;
			font-family: 'Syne', sans-serif;
			font-weight: 800;
			font-size: clamp(3rem, 6.5vw, 5.4rem);
			line-height: 0.95;
			letter-spacing: -0.04em;
			color: var(--text);
			max-width: 12ch;
		}

		.hero p {
			margin: 0;
			max-width: 52rem;
			color: var(--muted);
			font-size: 1rem;
			line-height: 1.6;
		}

		div[data-testid="stForm"] {
			background: rgba(255, 255, 255, 0.78);
			border: 1px solid var(--border);
			border-radius: 24px;
			padding: 1.1rem 1.1rem 0.9rem;
			backdrop-filter: blur(18px);
			box-shadow: 0 24px 60px rgba(15, 23, 42, 0.08);
		}

		div[data-testid="stTextInput"] label {
			font-weight: 600;
			color: var(--text);
		}

		div[data-testid="stTextInput"] input {
			border-radius: 16px;
			border: 1px solid rgba(37, 99, 235, 0.15);
			background: rgba(255, 255, 255, 0.94);
			color: var(--text);
			padding: 0.85rem 1rem;
			box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.75);
		}

		div[data-testid="stTextInput"] input::placeholder {
			color: rgba(91, 102, 122, 0.78);
			opacity: 1;
		}

		div[data-testid="stTextInput"] input:focus {
			background: rgba(255, 255, 255, 1);
			color: var(--text);
		}

		div[data-testid="stButton"] > button {
			width: 100%;
			border: 1px solid #09090F !important;
			border-radius: 999px;
			padding: 0.85rem 1.25rem;
			background: #09090F !important;
			color: #FFFFFF !important;
			font-weight: 700;
			letter-spacing: 0.02em;
			box-shadow: 0 16px 32px rgba(15, 23, 42, 0.18);
			transition: transform 0.18s ease, box-shadow 0.18s ease, background 0.18s ease, color 0.18s ease, border-color 0.18s ease;
		}

		div[data-testid="stButton"] > button:hover {
			background: #FFFFFF !important;
			color: #09090F !important;
			border-color: #09090F !important;
			transform: translateY(-1px);
			box-shadow: 0 18px 38px rgba(15, 23, 42, 0.12);
		}

		div[data-testid="stTabs"] {
			margin-top: 0.75rem;
		}

		div[data-baseweb="tab-list"] {
			gap: 0.5rem;
			padding-bottom: 0.35rem;
		}

		button[data-baseweb="tab"] {
			border-radius: 999px !important;
			border: 1px solid var(--border) !important;
			background: rgba(255, 255, 255, 0.72) !important;
			color: var(--muted) !important;
			padding: 0.5rem 0.9rem !important;
			font-weight: 600 !important;
		}

		button[data-baseweb="tab"][aria-selected="true"] {
			background: linear-gradient(135deg, rgba(37, 99, 235, 0.12), rgba(6, 182, 212, 0.12)) !important;
			color: var(--text) !important;
			border-color: rgba(37, 99, 235, 0.18) !important;
		}

		div[data-testid="stExpander"] {
			border-radius: 18px;
			border: 1px solid var(--border);
			background: rgba(255, 255, 255, 0.7);
		}

		.stAlert {
			border-radius: 18px;
		}

		.stMarkdown,
		.stText,
		.stCaption {
			color: var(--text);
		}
		</style>
		""",
		unsafe_allow_html=True,
	)


def as_text(value: object) -> str:
	if value is None:
		return ""
	if isinstance(value, str):
		return value
	return str(value)


inject_styles()

st.markdown(
	"""
	<div class="hero">
		<span class="eyebrow">MULTI-AGENT RESEARCH SYSTEM</span>
		<h1>Research Mind</h1>
		<p>Deep research, one topic at a time.</p>
	</div>
	""",
	unsafe_allow_html=True,
)

missing_keys = [key for key in ("GROQ_API_KEY", "TAVILY_API_KEY") if not os.getenv(key)]
if missing_keys:
	st.warning(f"Missing environment variables: {', '.join(missing_keys)}")

if "research_state" not in st.session_state:
	st.session_state.research_state = None

if "research_topic" not in st.session_state:
	st.session_state.research_topic = ""


with st.form("research_form", clear_on_submit=False):
	topic = st.text_input(
		"Topic",
		placeholder="e.g. solid-state batteries in consumer electronics",
	)
	submitted = st.form_submit_button("Run research")


if submitted:
	topic = topic.strip()
	if not topic:
		st.error("Enter a topic.")
	else:
		try:
			with st.spinner("Running the agents..."):
				state = run_research_pipeline(topic)
			st.session_state.research_topic = topic
			st.session_state.research_state = state
		except Exception as exc:
			st.error(f"Research run failed: {exc}")


state = st.session_state.research_state
if state:
	st.markdown(f"### {st.session_state.research_topic}")

	report_tab, critique_tab = st.tabs(["Report", "Critique"])

	with report_tab:
		st.markdown(as_text(state.get("report")))

	with critique_tab:
		st.markdown(as_text(state.get("critic_review")))
