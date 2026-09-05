# nz-credit-risk-analysis
# 🇳🇿 NZ Credit Risk Analysis: Personal Consumer NPL as a Leading Indicator of Housing NPL

## Overview
This project investigates whether Personal Consumer loan delinquency 
rates can serve as a leading indicator of housing loan delinquency 
in New Zealand, using publicly available data from the Reserve Bank 
of New Zealand (RBNZ).

Drawing on my background in credit risk model validation 
(Hyundai Capital NZ — AUROC, KS statistics, PSI) and financial 
compliance (ANZ Bank NZ — CCCFA remediation), this analysis applies 
time-series correlation techniques to assess the predictive 
relationship between consumer and housing loan non-performing 
loan (NPL) ratios.

## Business Question
New Zealand lenders are known to place limited weight on personal 
consumer loan delinquency when assessing mortgage applications. 
This analysis asks: does the data support a stronger role for 
consumer loan arrears as an early warning signal for housing loan 
stress?

## Data Sources
- **RBNZ S50** — Banks: Assets – Non-performing loan ratios 
  (Dec 2008 – current) | rbnz.govt.nz
- **RBNZ B2** — Wholesale Interest Rates, Monthly close 
  (2018 – current) | rbnz.govt.nz
- Analysis period: January 2020 – July 2026 (79 months)

## Tools Used
- **Python** (pandas, matplotlib, scipy)
- **SQLite** — data storage
- **Jupyter Notebook** — documented analysis workflow
- **Pearson Cross-Correlation** — lag analysis
- **Time-series visualisation** — multi-axis trend analysis

## Key Findings
- Personal Consumer NPL shows a statistically significant positive 
  correlation with Housing NPL at a 3-month lag 
  (r = 0.335, p = 0.003)
- Visual analysis confirms Personal Consumer NPL tends to rise and 
  fall ahead of Housing NPL, particularly around the OCR hiking 
  cycle (2022–2023) and subsequent easing (2024–2025)
- However, as Personal Consumer NPL is an aggregated indicator 
  (comprising credit cards, personal loans, auto loans, and BNPL), 
  further analysis at the sub-category level may reveal stronger 
  leading relationships

## Limitations & Next Steps
The Personal Consumer NPL used in this analysis is an aggregated 
measure across multiple product types. Disaggregated data by product 
(e.g. credit card arrears, auto loan arrears) from providers such 
as Centrix may reveal stronger or more specific leading indicators 
of housing loan stress. This is identified as a direction for 
further analysis.

## Skills Demonstrated
- Time-series analysis with lag correlation
- Cross-variable financial risk analysis using public data
- Statistically grounded interpretation of results
- Honest acknowledgement of data limitations and next analytical steps
- Domain knowledge in NZ credit risk and regulatory environment
