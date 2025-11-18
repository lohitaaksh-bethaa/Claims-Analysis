import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------
# 1. LOAD DATA
# ------------------------------------------
df = pd.read_csv("C:\\Users\\Lohit\\Documents\\Projects to do\\HealthcareAnalytics\\claims_data.csv")

# ------------------------------------------
# 2. DATA CLEANING
# ------------------------------------------
df['Date of Service'] = pd.to_datetime(df['Date of Service'], errors='coerce')

num_cols = ['Billed Amount', 'Allowed Amount', 'Paid Amount']
df[num_cols] = df[num_cols].apply(pd.to_numeric, errors='coerce')

cat_cols = [
    'Claim Status','Outcome','Reason Code','Follow-up Required',
    'AR Status','Insurance Type','Provider ID','Procedure Code','Diagnosis Code'
]

for col in cat_cols:
    df[col] = df[col].astype(str).str.strip().replace({'nan': 'Unknown', 'None': 'Unknown'})

# ------------------------------------------
# 3. BASIC KPIs
# ------------------------------------------
total_claims = df['Claim ID'].nunique()
total_billed = df['Billed Amount'].sum()
total_allowed = df['Allowed Amount'].sum()
total_paid = df['Paid Amount'].sum()

avg_billed = df['Billed Amount'].mean()
avg_paid = df['Paid Amount'].mean()

paid_claims = df[df['Claim Status'] == "Paid"]['Claim ID'].nunique()
denied_claims = df[df['Claim Status'] == "Denied"]['Claim ID'].nunique()

denial_rate = denied_claims / total_claims

write_off_total = total_billed - total_allowed
write_off_pct = write_off_total / total_billed

allowed_to_billed = total_allowed / total_billed
paid_to_allowed = total_paid / total_allowed

# Print KPIs
print("===== CLAIMS KPI SUMMARY =====")
print("Total Claims:", total_claims)
print("Total Billed Amount:", total_billed)
print("Total Allowed Amount:", total_allowed)
print("Total Paid Amount:", total_paid)
print("Average Billed:", avg_billed)
print("Average Paid:", avg_paid)
print("Paid Claims:", paid_claims)
print("Denied Claims:", denied_claims)
print("Denial Rate:", denial_rate)
print("Write-off Total:", write_off_total)
print("Write-off %:", write_off_pct)
print("Allowed-to-Billed Ratio:", allowed_to_billed)
print("Paid-to-Allowed Ratio:", paid_to_allowed)

# ------------------------------------------
# 4. GROUPED METRICS
# ------------------------------------------
provider_metrics = df.groupby('Provider ID').agg({
    'Claim ID':'nunique',
    'Billed Amount':'sum',
    'Allowed Amount':'sum',
    'Paid Amount':'sum'
})

insurance_metrics = df.groupby('Insurance Type').agg({
    'Claim ID':'nunique',
    'Billed Amount':'sum',
    'Allowed Amount':'sum',
    'Paid Amount':'sum'
})

procedure_metrics = df.groupby('Procedure Code').agg({
    'Claim ID':'nunique',
    'Billed Amount':'sum',
    'Paid Amount':'sum'
})

diagnosis_metrics = df.groupby('Diagnosis Code').agg({
    'Claim ID':'nunique',
    'Billed Amount':'sum',
    'Paid Amount':'sum'
})

# Print summaries
print("\n===== PROVIDER SUMMARY =====")
print(provider_metrics.head())

print("\n===== INSURANCE SUMMARY =====")
print(insurance_metrics.head())

print("\n===== PROCEDURE SUMMARY =====")
print(procedure_metrics.head())

print("\n===== DIAGNOSIS SUMMARY =====")
print(diagnosis_metrics.head())

# ------------------------------------------
# 5. MONTHLY TREND
# ------------------------------------------
df['Month'] = df['Date of Service'].dt.to_period('M').dt.to_timestamp()

monthly_trend = df.groupby('Month').agg({
    'Claim ID':'nunique',
    'Billed Amount':'sum',
    'Paid Amount':'sum'
})

print("\n===== MONTHLY TREND =====")
print(monthly_trend)

# ------------------------------------------
# 6. VISUALIZATIONS
# ------------------------------------------

# --- Financial summary (bar chart)
plt.figure(figsize=(6,4))
plt.bar(["Billed", "Allowed", "Paid"], [total_billed, total_allowed, total_paid])
plt.title("Financial Summary")
plt.ylabel("Amount")
plt.show()

# --- Claim status distribution (pie chart)
status_counts = df['Claim Status'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%')
plt.title("Claim Status Distribution")
plt.show()

# --- Monthly trend (line chart)
plt.figure(figsize=(10,5))
plt.plot(monthly_trend.index, monthly_trend['Billed Amount'], marker='o', label="Billed")
plt.plot(monthly_trend.index, monthly_trend['Paid Amount'], marker='o', label="Paid")
plt.title("Monthly Trend: Billed vs Paid")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()
plt.show()
