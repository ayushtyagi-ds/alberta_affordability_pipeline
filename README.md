# 🚀 Alberta Affordability Pipeline — End-to-End Data Engineering Project
*A Databricks, Delta Lake, and PySpark–powered analysis of affordability trends in Alberta.*

---

## 🧭 Project Overview
The **Alberta Affordability Pipeline** is a complete data engineering project built using **Databricks Medallion Architecture (Bronze → Silver → Gold)**.  
It integrates multiple real-world datasets — wages, inflation, rent, and unemployment — to calculate and visualize a unified **Affordability Index** that reflects the cost-of-living conditions in Alberta over time.

This project demonstrates:

- Modern **ETL pipeline engineering**  
- **Data modeling** using Delta Lake  
- **Feature engineering & metric creation**  
- **Interactive dashboarding**  
- **Actionable economic insights**

It is designed both as a **capstone project** and a **portfolio piece** to showcase end-to-end data engineering skills.

---

## 🏆 Key Features
- ✔ Automated ETL pipeline using PySpark  
- ✔ Clean Medallion architecture with Delta tables  
- ✔ Transformation logic for each dataset  
- ✔ A custom Affordability Index metric  
- ✔ Interactive Databricks dashboard (multi-page)  
- ✔ Correlation heatmap for deeper insights  
- ✔ Economic storytelling for technical + business audiences  

---

# 🏗️ Architecture — Medallion Pipeline

```
                ┌──────────────────────────┐
                │         Bronze            │
                │ Raw CPI, Wages, Rent,     │
                │ Unemployment Tables       │
                └────────────┬─────────────┘
                             │
            Cleaning, Casting, Filtering
                             ▼
                ┌──────────────────────────┐
                │         Silver            │
                │ Standardized + Aligned    │
                │ Monthly Economic Metrics  │
                └────────────┬─────────────┘
                             │
           Joining, Feature Engineering
                             ▼
                ┌──────────────────────────┐
                │          Gold             │
                │ Final Affordability Index │
                │ Dashboard-Ready Tables    │
                └──────────────────────────┘
```

---

# 📊 Datasets Used
| Dataset | Source | Purpose |
|--------|--------|---------|
| Wages (Average Weekly Earnings) | StatsCan | Measures purchasing power |
| CPI (Inflation Rate) | StatsCan | Tracks cost-of-living increases |
| Rent Change (2BR Unit) | Alberta Open Data | Captures housing pressure |
| Unemployment Rate | StatsCan | Indicates economic stability |

---

# 🧮 Affordability Index Formula

\[
	extbf{Affordability Index} = 	ext{Wage Growth} - (	ext{Inflation} + 	ext{Rent Change} + 	ext{Unemployment Change})
\]

### Interpretation
- **Higher Index → More affordable conditions**
- **Lower / Negative Index → Cost pressure on Albertans**
- This composite metric tells a more complete story than any individual dataset.

---

# 📈 Dashboard Overview (3 Pages)

## 📄 Page 1 — Affordability Trends
- Monthly Affordability Index (line)  
- Yearly averages (bar)  

## 📄 Page 2 — Economic Drivers
- Wage Growth vs Inflation  
- Rent Change (%) over time  
- Rent Change vs Affordability scatter  

## 📄 Page 3 — Correlations & Deep Insights
- Affordability Regime Clusters  
- Full correlation heatmap  
- Driver ranking  

---

# 📈 Business Insights (Executive Summary)

### 🔻 Inflation and rent are the biggest affordability pressures  
### 📉 Wage growth has not kept up  
### 📈 2021 showed a temporary improvement  
### 🟥 Unemployment shocks amplify affordability declines  
### 🔁 Alberta’s affordability is cyclical, not stable  

---

# 👥 What This Means for Everyday Albertans

### 🏠 Rent increases hit households hardest  
### 🛒 Inflation reduces purchasing power quickly  
### 💼 Job stability matters  
### 💸 Slow wage growth isn’t enough  
### 🔁 Affordability improves… then declines again  

This project converts complex economic signals into simple insights that everyday Albertans can understand.

---

# 📜 Repository Structure

```
alberta_affordability_pipeline/
│
├── notebooks/
│   ├── 1_bronze_ingestion.ipynb
│   ├── silver_transformations/
│   ├── gold_affordability_index.ipynb
│   └── dashboard_visualizations.ipynb
│
├── dashboard/
│   └── Alberta Affordability Dashboard.lvdash.json
│
└── README.md
```

---

# 🛠️ Technologies Used
- Databricks  
- Unity Catalog + Volumes  
- PySpark / Spark SQL  
- Delta Lake  
- Seaborn / Matplotlib  
- Databricks SQL Dashboards  
- GitHub Version Control  

---

# 🚀 How to Run the Project

### Step 1 — Clone the Repository
```
git clone https://github.com/ayushtyagi-ds/alberta_affordability_pipeline.git
```

### Step 2 — Import into Databricks  
Upload notebooks to your workspace.

### Step 3 — Create Catalog & Schema
```sql
CREATE CATALOG IF NOT EXISTS mycatalog;
CREATE SCHEMA IF NOT EXISTS mycatalog. default;
```

### Step 4 — Run Pipeline
1. Bronze ingestion  
2. Silver transformations  
3. Gold Affordability Index  
4. Visualization notebook  

### Step 5 — Open Dashboard  
Load the `.lvdash.json` file into Databricks SQL → Dashboards.

---

# 🧩 Future Enhancements
- Streamlit Web App  
- Machine Learning forecasting  
- Weighted Affordability Index  
- More granular municipal-level datasets  
- Automated daily data ingestion  

---

# ✨ Author
**Ayush Tyagi**  
Data Engineering & BI Developer  
GitHub: https://github.com/ayushtyagi-ds
