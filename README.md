Live demo: https://nz-npl-monitor.streamlit.app

# nz-credit-risk-analysis
🇳🇿 NZ Credit Risk Analysis: Exploring Personal Consumer NPL as a Possible Leading Indicator of Housing NPL

## Data Source
- RBNZ S50: Banks – Assets – Loans by asset quality (Non-performing loan ratios)
- Official page: https://www.rbnz.govt.nz/statistics/series/registered-banks/banks-assets-loans-by-asset-quality
- Long-run NPL ratios file (Dec 2008 – current) available as XLSX on the same page
- Analysis period used: Jan 2020 – Jul 2026 (approx.)

## Overview
This project explores whether Personal Consumer loan delinquency rates show a statistical lead-lag relationship with housing loan delinquency in New Zealand, using publicly available data from the Reserve Bank of New Zealand (RBNZ).

Drawing on my background in credit risk model validation (Hyundai Capital NZ — AUROC, KS statistics, PSI) and financial compliance (ANZ Bank NZ — CCCFA remediation), this analysis applies time-series correlation techniques to examine the relationship between consumer and housing loan non-performing loan (NPL) ratios. The analysis is correlational, not causal — see Limitations below.

## Business Question
New Zealand lenders are known to place limited weight on personal consumer loan delinquency when assessing mortgage applications. This analysis asks: does the data show a measurable lagged correlation between consumer loan arrears and housing loan stress — one that could be worth monitoring as an early-warning signal, even without implying a causal relationship?

## Hypothesis
Personal Consumer NPL may show a positive lagged correlation with Housing NPL, possibly most visible around the OCR hiking cycle (2022–2023) and the subsequent easing period. This is treated as an exploratory hypothesis to test, not an assumed causal mechanism.

## Validation Approach
- Pearson cross-correlation across a range of lags (1–12 months), not a single lag chosen after the fact
- Visual inspection of both time series together with the OCR cycle
- Note: both series are macro time series with long-run trends, so correlation alone can be inflated by shared trend rather than a genuine lead-lag relationship (see Limitations)
- Stationarity checks (ADF, KPSS) on both NPL series
- Sensitivity check: Pearson lag correlation on first-differenced series
## Data Sources
- RBNZ S50 — Banks: Assets – Non-performing loan ratios (Dec 2008 – current) | rbnz.govt.nz
- RBNZ B2 — Wholesale Interest Rates, Monthly close (2018 – current) | rbnz.govt.nz
- Analysis period: January 2020 – July 2026 (79 months)

## Tools Used
- Python (pandas, matplotlib, scipy)
- SQLite — data storage
- Jupyter Notebook — documented analysis workflow
- Pearson Cross-Correlation — lag analysis across multiple lags
- Time-series visualisation — multi-axis trend analysis
- Python (pandas, matplotlib, scipy, statsmodels)
## Key Findings
- Personal Consumer NPL shows a statistically significant positive **correlation** with Housing NPL at a 3-month lag (r = 0.335, p = 0.003), the strongest among the lags tested (1–12 months)
- Visually, Personal Consumer NPL and Housing NPL move in the same general direction around the OCR hiking cycle (2022–2023) and subsequent easing (2024–2025); this is consistent with — but does not confirm — a leading relationship
- As Personal Consumer NPL is an aggregated indicator (comprising credit cards, personal loans, auto loans, and BNPL), further analysis at the sub-category level may reveal stronger or weaker leading relationships
- At **levels**, Personal Consumer NPL shows a significant positive correlation with Housing NPL at a 3-month lag (r = 0.335, p = 0.003), the strongest among lags 1–12
- **ADF / KPSS** on the analysis window: Personal Consumer NPL gives mixed signals (ADF p = 0.43, KPSS p = 0.10); Housing NPL looks non-stationary (ADF p = 0.68, KPSS p = 0.01)
- After **first differencing**, the lag-3 correlation falls to r = 0.039 (p = 0.74) and is not significant
- The level result is therefore treated as exploratory and possibly trend-driven, not as evidence of a robust short-run leading indicator
## Limitations & Next Steps
- **Correlation, not causation**: a positive lagged correlation does not establish that consumer NPL *causes* or *predicts* housing NPL. Both series may be jointly driven by a common factor (e.g. OCR changes, cost-of-living pressure, unemployment) rather than one leading the other.
- **Trend/spurious correlation risk**: both series trend over the 2020–2026 period, which can inflate correlation estimates. * **Trend / spurious correlation:** ADF and KPSS were run on both series. Housing NPL is non-stationary on both tests; Consumer NPL is mixed. The significant level correlation at lag 3 (r = 0.335) does **not** survive first differencing (r = 0.039, p = 0.74), which is consistent with shared trends or common macro factors rather than a stable lead-lag relationship in period-to-period changes.
- **Reverse causality is not ruled out**: housing-related financial stress
