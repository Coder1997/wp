import streamlit as st
from openai import OpenAI
import os

# --- CONFIG ---
# Set your OpenAI API key in the OPENAI_API_KEY environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = "gpt-4o"

# --- UI ---
st.title("🧠 Virtual PM Twin Interview")
st.caption("Conduct qualitative interviews with a memory-grounded synthetic PM persona")

# Load twin memory
DEFAULT_MEMORY = """
You are a virtual product manager. Your behavior is based on interviews with multiple real B2B SaaS PMs.

Your core beliefs:
- Deliver customer value over internal politics
- Bias toward speed and iteration
- Use data as a guide, but not a dictator

Your decision style:
- Prioritize high-impact, low-effort wins
- Default to MVP unless design strongly pushes for polish
- Align roadmap with sales and leadership pressure

Your tools and workflows:
- Uses Jira, Notion, Amplitude, Loom, Slack
- Trusts engineers; expects async collaboration

Your success metrics:
- Activation and adoption
- NPS uplift
- Reduction in churn triggers

You will now answer questions from a product researcher. Respond in natural, thoughtful language as if you're speaking live.
"""

memory = st.text_area("🧠 Twin Memory (editable)", value=DEFAULT_MEMORY, height=300)

st.markdown("---")
st.subheader("🗣️ Interview")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": memory},
        {"role": "user", "content": "Let’s begin. Tell me a little about your role and your team."}
    ]

for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
if prompt := st.chat_input("Ask a question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Get model response
    with st.spinner("Thinking like a PM twin..."):
        response = client.chat.completions.create(
            model=MODEL,
            messages=st.session_state.messages,
            temperature=0.8
        )
        msg = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
