import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="Resilience Forge", layout="wide")

# Define resilience factors and default values
factors = {
    "Cohesion and Trust": 5,
    "Leadership and Decision-Making": 5,
    "Financial and Resource Buffering": 5,
    "Innovation and Learning": 5,
    "Community and Customer Connection": 5,
    "Adaptability to Change": 5
}

factor_descriptions = {
    "Cohesion and Trust": "How well your team works together, shares information, and supports one another.",
    "Leadership and Decision-Making": "Clarity, transparency, and confidence in leadership and decision processes.",
    "Financial and Resource Buffering": "Capacity to absorb shocks through savings, redundancy, or emergency resources.",
    "Innovation and Learning": "Openness to new ideas, experimentation, and continuous learning.",
    "Community and Customer Connection": "Strength of relationships and feedback loops with key stakeholders.",
    "Adaptability to Change": "Ability to pivot operations, roles, or services in response to shifts."
}

st.title("Resilience Forge")
st.markdown("""
Welcome to **Resilience Forge** — a practical tool to help businesses and community organisations **enhance their resilience**.

Use the sliders below to assess your current resilience strengths and areas for growth across six key factors.
""")

# Option to use custom weights
use_weights = st.checkbox("Use custom weights for each factor 🧮")
st.caption("Turn this on if you want some factors to count more than others in your resilience score.")
weights = {}

st.markdown("### 🎛️ Adjust Each Resilience Factor")

user_inputs = {}
notes = {}

for factor, default in factors.items():
    col1, col2 = st.columns([2, 3])
    with col1:
        st.markdown(f"**{factor}** ℹ️")
        st.caption(factor_descriptions[factor])
        user_inputs[factor] = st.slider(
            label="",
            min_value=1,
            max_value=10,
            value=default,
            step=1,
            key=factor
        )
    with col2:
        notes[factor] = st.text_input(f"📝 Notes for {factor}", placeholder="E.g., planning a team retreat...")
    if use_weights:
        st.caption("⚖️ Weight determines how important this factor is in the final score.")
        weights[factor] = st.slider(f"Weight for {factor}", 1, 10, 5, key=f"weight_{factor}")
    else:
        weights[factor] = 1

# Calculate weighted resilience score
weighted_values = [user_inputs[f] * weights[f] for f in factors]
total_weight = sum(weights.values())
average_score = sum(weighted_values) / total_weight

# Display score in a progress circle (Plotly gauge chart)
st.markdown("## 📊 Your Resilience Score")
fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = average_score,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Resilience Score (out of 10)"},
    gauge = {
        'axis': {'range': [0, 10], 'tickwidth': 1, 'tickcolor': "darkblue"},
        'bar': {'color': "royalblue"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 3], 'color': '#ffcccc'},
            {'range': [3, 7], 'color': '#ffe699'},
            {'range': [7, 10], 'color': '#c6efce'}
        ]
    }
))

st.plotly_chart(fig, use_container_width=True)

# Toolkit and Tips section
st.markdown("### 🧰 Resilience Toolkit")
with st.expander("💡 Tips for Enhancing Each Factor"):
    st.markdown("""
- **Cohesion and Trust**: Host regular team catch-ups. Celebrate small wins. Provide clear communication.
- **Leadership and Decision-Making**: Empower staff to make decisions. Use transparent processes.
- **Financial and Resource Buffering**: Maintain emergency funds. Optimise inventory and overheads.
- **Innovation and Learning**: Encourage experimentation. Document and share lessons learned.
- **Community and Customer Connection**: Seek feedback. Be visible and responsive in your community.
- **Adaptability to Change**: Run scenario planning. Upskill staff for agility.
    """)

# Strategy Summary
st.markdown("### 📋 Your Resilience Strategy Summary")
with st.expander("📄 View Summary of Your Current Plan"):
    for factor in factors:
        st.markdown(f"**{factor}**: {user_inputs[factor]} / 10")
        if notes[factor]:
            st.markdown(f"_Note_: {notes[factor]}")
        st.markdown("---")

# Instructions section
st.markdown("### 🧭 Make the Most of Resilience Forge")
with st.expander("📘 How This Tool Works"):
    st.markdown("""
1. **Sliders**: Set your current perceived level (1–10) for each of the six resilience factors.
2. **Notes**: Add notes beside each factor to capture insights, plans, or context.
3. **Custom Weights**: Use this to prioritise some factors over others in your final score.
4. **Score Gauge**: View your calculated average score on a visual dial.
5. **Tips & Toolkit**: Read practical suggestions for boosting each factor.
6. **Summary & PDF (coming soon)**: Review your full strategy and export it to PDF.
    """)

# Footer
st.markdown("""
---
*Resilience Forge helps you visualise and strengthen the capabilities that allow your enterprise to adapt, recover, and thrive in uncertainty.*
""")
