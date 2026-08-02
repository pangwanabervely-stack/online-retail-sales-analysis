# Online Retail Sales & Customer Analysis

**Author:** Bervely Pangwana
**Tools used:** Python (pandas, matplotlib, seaborn), Power BI / Tableau

## Project Overview
This project analyzes real transactional data from a UK-based online retailer
(Online Retail II dataset, UCI Machine Learning Repository) to uncover revenue
trends, top-performing products and markets, and customer purchasing behavior.

## Objectives
- Clean and prepare messy real-world transactional data
- Identify revenue trends over time
- Determine top products and countries by revenue
- Segment customers using RFM (Recency, Frequency, Monetary) analysis
- Present findings through an interactive dashboard

## Data Source
[Online Retail II — UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/502/online+retail+ii)

## Methodology
1. **Data Cleaning:** Removed cancelled orders, missing customer IDs, and
   invalid quantity/price entries using pandas.
2. **Exploratory Data Analysis:** Analyzed monthly revenue trends, top
   products, and top countries by revenue.
3. **Customer Segmentation:** Applied RFM analysis to classify customers
   into segments (High Value, Regular, At Risk, New Customer).
4. **Dashboard:** Built an interactive dashboard in [Power BI/Tableau] to
   visualize revenue trends and customer segments for business stakeholders.

## Key Findings

**Data Quality:**
Of the original 525,461 transaction records, approximately 24% (124,545 rows) were removed during cleaning  primarily due to missing customer identifiers (~20% of all rows), cancelled orders, and invalid quantity/price entries. This reflects the real-world messiness typical of transactional retail data.

**Revenue Trend:**
Monthly revenue peaked in **November 2010 at £1,166,460**, consistent with pre-holiday wholesale restocking by this retailer's largely business-to-business customer base. December 2010 shows the lowest recorded revenue (£310,656), but this reflects a partial month in the dataset rather than an actual sales decline, since the data cuts off early in December.

**Top Products:**
The **WHITE HANGING HEART T-LIGHT HOLDER** was the top-selling product by revenue, generating approximately **£151,339**. Top sellers were dominated by home decor and gift/novelty items, reflecting the retailer's core product category.

**Geographic Concentration:**
Revenue is heavily concentrated in the **United Kingdom (£7,381,644)**, reflecting the retailer's domestic customer base. The next-largest market, **EIRE (Ireland)**, contributed a much smaller £356,042 roughly 5% of UK revenue  highlighting limited but present international demand, particularly from neighboring European countries.

**Customer Segmentation (RFM Analysis):**
Out of 4,312 unique customers:
- **Regular customers: 2,004 (46%)**
- **At Risk: 1,015 (24%)**
- **High Value: 926 (21%)**
- **New Customers: 367 (9%)**

Nearly a quarter of the customer base falls into the "At Risk" segment, representing a significant re-engagement opportunity, while High Value customers (21%) represent a smaller but disproportionately important group worth prioritizing for retention efforts.

## Dashboard

An interactive Power BI dashboard was built from the cleaned data and RFM
segments, covering sales performance and customer segmentation across two
report pages.

### Page 1 — Sales Overview
![Sales Overview Dashboard](dashboard_screenshots/page1_sales_overview.png)

Shows overall revenue trends, top products, and geographic breakdown, with
headline KPIs (total revenue, total orders, total customers) and a callout
insight: UK accounts for 84% of total revenue, and November is the peak
sales month.

### Page 2 — Customer Segmentation (RFM Analysis)
![Customer Segmentation Dashboard](dashboard_screenshots/page2_customer_segmentation.png)

Breaks customers into four segments (Regular, At Risk, High Value, New
Customer) based on Recency, Frequency, and Monetary value, with an
interactive slicer and a segment profile table showing the average
Recency/Frequency/Monetary per segment validating that the segmentation
behaves as expected (e.g. High Value customers order frequently, spend the
most, and purchased most recently).

The full interactive file is available as `dashboard.pbix` in this
repository (requires Power BI Desktop, free, to open).

## Files in this Repository
- `Online_Retail_Analysis.ipynb` — Jupyter notebook: data cleaning, EDA, and RFM analysis
- `cleaned_retail_data.csv` — too large for GitHub; [available via Google Drive](https://drive.google.com/file/d/1jyf67JD4djzdwK_Yeijgj_cB2lbM6Hip/view?usp=sharing)
- `customer_rfm_segments.csv` — customer segments output
- `dashboard.pbix` — Power BI dashboard file
- `dashboard_screenshots/` — screenshots of both dashboard pages
- Chart images (`monthly_revenue.png`, `top_products.png`, `top_countries.png`, `customer_segments.png`)

## How to Run
1. Download the dataset from the link above
2. Install requirements: `pip install pandas matplotlib seaborn openpyxl jupyter`
3. Open and run `Online_Retail_Analysis.ipynb` cell by cell (or download the pre-cleaned data from the [Google Drive link](https://drive.google.com/file/d/1jyf67JD4djzdwK_Yeijgj_cB2lbM6Hip/view?usp=sharing) above to skip straight to analysis)
4. Open `dashboard.pbix` in Power BI Desktop (free) to explore the interactive dashboard, or view the screenshots above
