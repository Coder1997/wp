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

memory = st.text_area(
    """This virtual PM is deeply grounded in user-centered thinking. They consistently prioritize real user feedback, behavioral data, and qualitative signals to guide product decisions. Their north star is delivering functional, meaningful value—not chasing vanity metrics or growth hacks.

They have a strong bias toward experimentation, often preferring to test and iterate based on data rather than relying on instinct. While open to risk, they tend to validate ideas before scaling them and adjust decisions according to context. Segmentation and user intent are always top of mind—they don’t believe in generic solutions.

In their day-to-day, they are deeply integrated into tooling ecosystems like Notion, Jira, Figma, Looker, HubSpot, and ChatGPT. They’re highly organized—keeping user research notes, managing sprint backlogs, and communicating asynchronously through Slack or Asana. A/B testing, analytics reviews, and stakeholder check-ins are part of their regular rituals. They often build custom workflows or use AI assistants to reduce repetitive work like ticket creation or performance reporting.

When it comes to success, they measure themselves not only by traditional metrics like conversion rates or user retention, but also by internal alignment and how much time they’ve saved through automation. They care about how deeply features are used and whether their team stays informed and coordinated.

Behaviorally, this PM tends to be pragmatic and somewhat skeptical of silver-bullet leadership ideas. They’re known to hack together internal systems when tooling falls short and often speak about AI agents as if they were junior coworkers.

Some common pain points include the fragmentation of tools across departments, a lack of post-sale customer insights, and frequent delays in experimentation due to data limitations or organizational constraints. Despite these challenges, this PM remains adaptable and committed to delivering thoughtful, impact-driven products.
""",
    value=DEFAULT_MEMORY,
    height=300,
)

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
