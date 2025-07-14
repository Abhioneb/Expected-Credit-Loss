import streamlit as st
from backend.service import load_data, compute_ecl, recommend_action

# Title
st.title("ECL Curve MVP")

# Load data once
df = load_data("data/loans.csv")
segments = df["segment_tag"].unique().tolist()

# Sidebar for selection
seg = st.sidebar.selectbox("Select segment", segments)

# Compute and plot
ecl = compute_ecl(df, seg)
st.line_chart(ecl.astype(float), use_container_width=True)

# Display recommendation
action = recommend_action(ecl)
st.markdown(f"### Recommended action: **{action}**")