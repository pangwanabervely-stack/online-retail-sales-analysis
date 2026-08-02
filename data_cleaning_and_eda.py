"""
Project: Online Retail Sales & Customer Analysis
Author: Bervely Pangwana
Dataset: Online Retail II (UCI ML Repository)
https://archive.ics.uci.edu/dataset/502/online+retail+ii

STEP 1: Download the .xlsx file from the link above and place it in the
same folder as this script. It has two sheets: "Year 2009-2010" and
"Year 2010-2011". You can start with just one sheet, or combine both.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. LOAD DATA
# -----------------------------
# Update the filename below to match your downloaded file
df = pd.read_excel("online_retail_II.xlsx", sheet_name="Year 2009-2010")

print("Initial shape:", df.shape)
print(df.head())
print(df.info())

# -----------------------------
# 2. CLEAN DATA
# -----------------------------

# Remove rows with missing Customer ID (can't attribute these to a customer)
df = df.dropna(subset=["Customer ID"])

# Remove cancelled orders (Invoice numbers starting with "C")
df = df[~df["Invoice"].astype(str).str.startswith("C")]

# Remove rows with non-positive Quantity or Price (returns/errors/free items)
df = df[(df["Quantity"] > 0) & (df["Price"] > 0)]

# Remove exact duplicate rows
df = df.drop_duplicates()

# Create a TotalPrice column
df["TotalPrice"] = df["Quantity"] * df["Price"]

# Make sure InvoiceDate is a proper datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

print("\nCleaned shape:", df.shape)

# -----------------------------
# 3. EXPLORATORY ANALYSIS
# -----------------------------

# Revenue over time (monthly)
monthly_revenue = df.set_index("InvoiceDate").resample("M")["TotalPrice"].sum()

plt.figure(figsize=(10, 5))
monthly_revenue.plot(kind="line", marker="o")
plt.title("Monthly Revenue")
plt.ylabel("Revenue (£)")
plt.xlabel("Month")
plt.tight_layout()
plt.savefig("monthly_revenue.png")
plt.close()

# Top 10 products by revenue
top_products = (
    df.groupby("Description")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_products.values, y=top_products.index)
plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue (£)")
plt.tight_layout()
plt.savefig("top_products.png")
plt.close()

# Top 10 countries by revenue (excluding UK to see international spread, optional)
top_countries = (
    df.groupby("Country")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title("Top 10 Countries by Revenue")
plt.xlabel("Revenue (£)")
plt.tight_layout()
plt.savefig("top_countries.png")
plt.close()

# -----------------------------
# 4. RFM ANALYSIS (Recency, Frequency, Monetary)
# -----------------------------
# This segments customers - a real technique used in marketing/BI roles

snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

rfm = df.groupby("Customer ID").agg(
    Recency=("InvoiceDate", lambda x: (snapshot_date - x.max()).days),
    Frequency=("Invoice", "nunique"),
    Monetary=("TotalPrice", "sum"),
)

# Score each dimension 1-5 (5 = best)
rfm["R_Score"] = pd.qcut(rfm["Recency"], 5, labels=[5, 4, 3, 2, 1])
rfm["F_Score"] = pd.qcut(rfm["Frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
rfm["M_Score"] = pd.qcut(rfm["Monetary"], 5, labels=[1, 2, 3, 4, 5])

rfm["RFM_Score"] = (
    rfm["R_Score"].astype(str) + rfm["F_Score"].astype(str) + rfm["M_Score"].astype(str)
)

# Simple segment labeling (customize this once you see your own data)
def segment_customer(row):
    if row["R_Score"] >= 4 and row["F_Score"] >= 4 and row["M_Score"] >= 4:
        return "High Value"
    elif row["R_Score"] <= 2 and row["F_Score"] <= 2:
        return "At Risk"
    elif row["F_Score"] <= 2 and row["R_Score"] >= 4:
        return "New Customer"
    else:
        return "Regular"

rfm["Segment"] = rfm.apply(segment_customer, axis=1)

print("\nCustomer segments:")
print(rfm["Segment"].value_counts())

# -----------------------------
# 5. EXPORT CLEANED DATA FOR POWER BI / TABLEAU
# -----------------------------
df.to_csv("cleaned_retail_data.csv", index=False)
rfm.to_csv("customer_rfm_segments.csv")

print("\nDone. Files exported: cleaned_retail_data.csv, customer_rfm_segments.csv")
print("Charts saved: monthly_revenue.png, top_products.png, top_countries.png")
