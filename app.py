import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
import plotly.graph_objects as go

st.set_page_config(
    page_title="NZ NPL Leading Indicator Monitor",
    layout="wide"
)

st.title("🇳🇿 NZ NPL Leading Indicator Monitor")
st.caption(
    "Explore whether Personal Consumer NPL leads Housing NPL under different lag assumptions."
)

st.info(
    "Minimal interactive extension of the credit-risk analysis. "
    "For exploration and discussion — not a production risk model."
)

# ── Sidebar ──────────────────────────────────────────────
st.sidebar.header("Settings")
lag_months = st.sidebar.slider("Lag (months)", min_value=0, max_value=6, value=3)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "**Data:** RBNZ S50 (Non-performing loan ratios)\n\n"
    "**Limitation:** Personal Consumer NPL is aggregated "
    "(credit cards, personal loans, auto, BNPL)."
)

# ── Load & clean RBNZ S50 long-run file ──────────────────
@st.cache_data
def load_npl_data():
    # Skip title/notes/unit/series rows (RBNZ layout)
    raw = pd.read_excel("hs50-long-run.xlsx", header=None, skiprows=5)

    # A=date, C=Housing, D=Personal consumer
    df = raw.iloc[:, [0, 2, 3]].copy()
    df.columns = ["date", "housing_npl", "consumer_npl"]

    # Handle both text dates ("Dec 2008") and Excel real dates
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["housing_npl"] = pd.to_numeric(df["housing_npl"], errors="coerce")
    df["consumer_npl"] = pd.to_numeric(df["consumer_npl"], errors="coerce")

    df = df.dropna(subset=["date", "housing_npl", "consumer_npl"])
    df = df.sort_values("date").reset_index(drop=True)

    # Same window as original analysis
    df = df[df["date"] >= "2020-01-01"].copy()

    if df.empty:
        raise ValueError("No rows left after cleaning — check skiprows or columns")

    return df


try:
    df = load_npl_data()
except Exception as e:
    st.error(f"Could not load data: {e}")
    st.stop()

st.success(f"Loaded {len(df)} monthly observations (from {df['date'].min().date()} to {df['date'].max().date()})")

# ── Chart ────────────────────────────────────────────────
st.subheader("1. Time series")
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df["date"], y=df["consumer_npl"],
    name="Personal Consumer NPL", mode="lines"
))
fig.add_trace(go.Scatter(
    x=df["date"], y=df["housing_npl"],
    name="Housing NPL", mode="lines"
))
fig.update_layout(
    height=420,
    xaxis_title="Date",
    yaxis_title="NPL ratio (%)",
    legend=dict(orientation="h", yanchor="bottom", y=1.02)
)
st.plotly_chart(fig, use_container_width=True)

# ── Lag correlation ──────────────────────────────────────
st.subheader("2. Correlation at selected lag")

def lag_corr(x, y, lag):
    """x leads y by `lag` months."""
    if lag == 0:
        a, b = x, y
    else:
        a = x.iloc[:-lag].reset_index(drop=True)
        b = y.iloc[lag:].reset_index(drop=True)
    if len(a) < 5:
        return np.nan, np.nan, 0
    r, p = stats.pearsonr(a, b)
    return float(r), float(p), len(a)

r, p, n = lag_corr(df["consumer_npl"], df["housing_npl"], lag_months)

c1, c2, c3 = st.columns(3)
c1.metric("Lag (months)", lag_months)
c2.metric("Pearson r", f"{r:.3f}" if pd.notna(r) else "n/a")
c3.metric("p-value", f"{p:.4f}" if pd.notna(p) else "n/a")
st.caption(f"Observations used: {n}")

# ── Interpretation ───────────────────────────────────────
st.subheader("3. Interpretation")

if pd.notna(r) and pd.notna(p):
    sig = "statistically significant" if p < 0.05 else "not statistically significant"
    direction = "positive" if r > 0 else "negative"
    st.markdown(
        f"""
- At a **{lag_months}-month** lag, correlation is **{direction}** (r = {r:.3f}) and is **{sig}** (p = {p:.4f}).
- Original analysis: r ≈ 0.335, p ≈ 0.003 at lag 3.
- Supports discussion of Personal Consumer NPL as an *early warning* signal — not a standalone underwriting trigger.
        """
    )
else:
    st.write("Not enough data points for this lag.")

st.markdown(
    """
**What this app is for**
- Interactively testing the leading-indicator hypothesis.

**What it is not for**
- Production credit decisions or product-level signals
  (Personal Consumer NPL is aggregated across cards, personal loans, auto, BNPL).
    """
)
