**📊 Insurance Claims Analysis – Power BI & Python**

A complete end-to-end analysis of hospital insurance claims data using Power BI, Python, and Excel.
This project includes data cleaning, KPI creation, advanced analytics, visualizations, and an interactive Power BI dashboard.


**📁 Project Overview
**
This repository contains:
1. Raw claims dataset (claims_data.csv)
2. Cleaned dataset (Power Query transformations)
3. Python-generated metrics and exploratory analysis
4. Power BI dashboard with financial, operational, and risk insights
5. KPIs, DAX measures, and formulas
6. Documentation on how to reproduce and extend the analysis


🧼 1. Data Cleaning

Data was cleaned and transformed using Power Query.
Steps performed:
1. Converted dates to proper Date type
2. Converted monetary fields to numeric
3. Trimmed and cleaned text columns
4. Standardized categorical fields (Paid / Denied / Under Review, etc.)
5. Removed duplicates based on Claim ID
6. Added optional calculated columns
7. Created a dedicated Date dimension table for time-intelligence DAX


📈 2. Key Metrics (KPIs)
Financial Metrics
- Total Billed Amount
- Total Allowed Amount
- Total Paid Amount
- Write-off Amount & %
- Paid-to-Allowed Ratio
- Allowed-to-Billed Ratio

Operational Metrics
- Total Claims
- Denied Claims & Denial Rate
- Follow-up Rate
- Claim Status Distribution

Advanced Analytics
- High-cost outlier detection
- Fraud suspicion indicators
- Procedure/Provider cost drivers
- Trend forecasting (Python)


📘 3. DAX Measures (Core)

- Total Claims = DISTINCTCOUNT(Claims[Claim ID])
- Total Billed = SUM(Claims[Billed Amount])
- Total Allowed = SUM(Claims[Allowed Amount])
- Total Paid = SUM(Claims[Paid Amount])
- Paid Claims = CALCULATE([Total Claims], FILTER(Claims, Claims[Claim Status]="Paid"))
- Denied Claims = CALCULATE([Total Claims], FILTER(Claims, Claims[Claim Status]="Denied"))
- Denial Rate = DIVIDE([Denied Claims], [Total Claims], 0)
- Write-off Total = [Total Billed] - [Total Allowed]
- Write-off % = DIVIDE([Write-off Total], [Total Billed], 0)
- Allowed to Billed Ratio = DIVIDE([Total Allowed], [Total Billed], 0)
- Paid to Allowed Ratio = DIVIDE([Total Paid], [Total Allowed], 0)
- High Cost Threshold = AVERAGE(Claims[Billed Amount]) + 2 * STDEVX.P(Claims, Claims[Billed Amount])

  

📊 4. Power BI Dashboard
Includes 4 pages:
1️⃣ Summary
- Claims KPIs
- Denial rate
- Write-off %
- Trend charts

2️⃣ Financial Analysis
- Billed vs Allowed vs Paid
- Waterfall chart
- Top-paying procedures/providers

3️⃣ Operational Insights
- Claim Status breakdown
- Denial reason analysis
- Provider performance

4️⃣ Risk & Outliers
- High-cost claims
- Suspicious activity patterns
- Scatter plot comparison (Billed vs Paid)


❤️ Acknowledgements
This project was made for analyzing hospital insurance claims with a focus on financial efficiency, process improvement, and risk analytics.


📣 Contributions
Feel free to fork, improve visual design, add new models (ML, forecasting), or submit PRs.
