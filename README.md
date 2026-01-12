# 🏥 Insurance Claims Analysis – Case Study

## 📌 Executive Summary
This case study explores insurance claims submitted by a healthcare provider in order to assess financial performance, identify operational inefficiencies, and understand denial patterns. Python was used for end-to-end data cleaning, KPI calculation, aggregation, and visualization.

The analysis helps healthcare organizations:
- Reduce claim denials  
- Improve billing accuracy  
- Optimize insurer relationships  
- Identify costly procedures and diagnoses  
- Improve revenue cycle efficiency  

---

## 🎯 Business Problem
Healthcare providers face increasing financial pressure due to:
- High denial rates  
- Reduced reimbursement  
- Documentation errors  
- Time-consuming manual follow-ups  

Claims data contains insights that can help resolve these issues — but only if analyzed correctly.

---

## 🗂️ Dataset Overview

**Fields Included:**

| Field | Description |
|-------|-------------|
| Claim ID | Unique claim identifier |
| Provider ID | Physician or facility |
| Patient ID | Unique patient identifier |
| Date of Service | Date care was delivered |
| Procedure Code | CPT/HCPCS code |
| Diagnosis Code | ICD code |
| Billed Amount | Total amount billed |
| Allowed Amount | Amount insurer agreed |
| Paid Amount | Final reimbursed amount |
| Claim Status | Paid, Denied, Under Review |
| AR Status | Open, Pending, On Hold, etc. |
| Reason Code | Denial explanation |
| Insurance Type | Medicare, Commercial, Self-Pay |
| Follow-up Required | Yes/No indicator |

---

## 🎯 Objectives

### Financial Analysis
- Compare billed vs allowed vs paid  
- Analyze write-offs  
- Identify high-cost procedures and diagnoses  

### Operational Analysis
- Denial rate  
- Follow-up requirement  
- Claim status distribution  
- AR status bottlenecks  

### Trend & Pattern Analysis
- Month-over-month trends  
- Provider performance variation  
- Insurance payer patterns  

---

## 🧪 Methodology

### 1. Data Cleaning
Performed using Pandas:
- Convert dates  
- Fix categorical values  
- Standardize labels  
- Convert financial fields to numeric  

### 2. KPI Computation
Using simple Pandas aggregations:
total_billed = df["Billed Amount"].sum()
denial_rate = denied_claims / total_claims
write_off_pct = (total_billed - total_allowed) / total_billed

### 3. Grouped Analysis
Analysis by:
1. Provider ID
2. Insurance Type
3. Procedure Code
4. Diagnosis Code

### 4.Trend Analysis
Created monthly metrics:
df["Month"] = df["Date of Service"].dt.to_period("M")

### 5. Visualizations
- Generated using Matplotlib:
- Financial summary bar chart
- Claim status pie chart
- Monthly trend line chart

## 📈 Key Findings
### 💰 Financial Findings
- Significant write-offs indicate a gap between billed and allowed amounts.
- Certain diagnoses and procedures account for disproportionate high costs.
- Paid amounts fluctuate depending on insurance type.

###🔧 Operational Findings
- Denial rate indicates room for improvement in coding/documentation.
- Some providers have higher follow-up requirements, signaling workflow issues.
- Denial reasons such as Authorization Not Obtained appear frequently.

###🧑‍⚕️ Provider Insights
- Variation in billing and denial patterns across providers.
- Some providers show consistently higher rejected claims.

###📅 Trend Insights
- Monthly claim volumes and payments fluctuate.
- Peak activity occurs in specific months, suggesting seasonality.

### 🛠 Tools Used
- Python: Pandas, NumPy, Matplotlib
- GitHub for version control
- CSV as primary data source

### 🎒 Limitations
- No timestamps for TAT (Turnaround Time) analysis
- Dataset synthetic; no PHI/PII
- No ML features in simplified script

### 🚀 Future Enhancements
## 1. Machine Learning
- Predict claim denials
- Forecast paid amounts

## 2. Power BI Dashboard
- Interactive visuals
- Provider drill-downs
- Denial driver insights

## 3. Streamlit Web App
- Upload CSV → instant analysis

## 4. FastAPI
- Build a denial prediction API

### 🏁 Conclusion
This project demonstrates how claims analytics can help healthcare providers:
- Improve revenue cycle performance
- Reduce operational inefficiencies
- Understand denial patterns
- Manage insurer relationships better
This foundation can be expanded into a full analytics platform for healthcare operations.

## Author
**Lohitaaksh Bethaa**  
Data Analyst

