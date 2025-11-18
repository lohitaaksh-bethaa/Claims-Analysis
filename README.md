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
```python
total_billed = df["Billed Amount"].sum()
denial_rate = denied_claims / total_claims
write_off_pct = (total_billed - total_allowed) / total_billed
