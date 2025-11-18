🧾 Overview
This project processes a healthcare insurance claims dataset and produces clean, easy-to-read metrics such as:
- Total claims
- Total billed, allowed, and paid amounts
- Average billed and paid amounts
- Paid vs denied claims
- Denial rate
- Write-off calculations
- Provider, insurance, diagnosis, and procedure summaries
- Monthly claim trends
- Visualization charts
- Financial summary
- Claim status distribution
- Monthly billed vs paid trend


🚀 Features
✔ Data Cleaning
- Converts dates to proper formats
- Standardizes categorical values
- Converts billing columns to numeric types

✔ KPI Calculations
- Total claims
- Paid, denied counts
- Billed, allowed, paid totals
- Write-off %
- Denial rate
- Efficiency ratios

✔ Grouped Analysis
- Provider-level metrics
- Insurance type summaries
- Procedure-wise and diagnosis-wise cost analysis

✔ Visualizations
- Bar chart: Billed vs Allowed vs Paid
- Pie chart: Claim Status distribution
- Line chart: Monthly trends

✔ No File Export
This version only prints dataframes and displays charts. Nothing is written to disk.

📝 Code Used in This Project
The script processes:
- Data cleaning
- KPI computation
- Grouped aggregations
- Monthly trends
- Visual charts
The full code is inside claims_analysis.py.

📜 Requirements
- Python 3.7+
- Libraries:
  - pandas
  - numpy
  - matplotlib
