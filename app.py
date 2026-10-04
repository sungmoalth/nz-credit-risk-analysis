import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats

st.set_page_config(
    page_title="NZ NPL Leading Indicator Monitor",
    layout="wide"
)

st.title("🇳🇿 NZ NPL Leading Indicator Monitor")
st.caption("Explore whether Personal Consumer NPL leads Housing NPL under different lag assumptions.")

st.info(
    "This is a minimal interactive extension of the credit-risk analysis. "
    "It is for exploration and discussion — not a production risk model."
)

# --- Sidebar ---
st.sidebar.header("Settings")
lag_months = st.sidebar.slider("Lag (months)", min_value=0, max_value=6, value=3)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "**Data:** RBNZ S50 (Non-performing loan ratios)\n\n"
    "**Limitation:** Personal Consumer NPL is aggregated "
    "(credit cards, personal loans, auto, BNPL)."
)

# --- Placeholder until data is wired ---
st.subheader("1. Time series")
st.write("Chart will appear here after data is connected.")

st.subheader("2. Correlation at selected lag")
st.write(f"Selected lag: **{lag_months} months**")
st.write("Correlation result will appear here.")

st.subheader("3. Interpretation")
st.markdown(
    """
    - Use the lag slider to test the leading-indicator hypothesis.
    - A statistically significant positive correlation at lag 3 was found in the original analysis (r ≈ 0.335, p ≈ 0.003).
    - Correlation strength alone is not enough for underwriting decisions.
    """
)
