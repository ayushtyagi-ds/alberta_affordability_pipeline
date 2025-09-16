# Alberta_affordability_pipeline

**Author:** Ayush Tyagi  
**Course:** Capstone Project (Fall 2025)  
**Tools:** Databricks, PySpark, Delta Lake, GitHub  

---

## 📌 Project Overview
This project builds an **automated data pipeline** to measure and track **affordability trends in Alberta**, focusing on the relationship between **wages, inflation (CPI), and housing costs**.  

The pipeline follows the **medallion architecture** (Bronze → Silver → Gold), using **PySpark** and **Delta Lake** on Databricks.  
The final output is an **Affordability Index** — a metric showing how wage growth compares against rising living costs, giving insights into the real financial health of Albertans.  

---

## 🎯 Goals
- Automate ingestion of open economic datasets (StatCan, CMHC, etc.)  
- Clean and standardize data across multiple sources (Bronze → Silver).  
- Create a **Gold dataset** with affordability insights (wages vs CPI vs housing).  
- Build an **Affordability Index** to summarize financial trends.  
- Deliver code and documentation via GitHub for reproducibility.  

---

## 🧑‍🤝‍🧑 User Persona
- **Prospective Albertan (job seeker or new resident)**  
  *"As a prospective Albertan, I need access to affordability trends (wages vs cost of living), so I can make an informed financial decision about relocating."*  

- **Policy maker/researcher**  
  *"I want to track affordability over time to better understand the impact of wages, inflation, and housing costs on Albertans."*  

---

## 🏗️ Technical Architecture
### Medallion Architecture
- **Bronze Layer:** Raw data ingestion (CSV/JSON from StatCan & CMHC).  
- **Silver Layer:** Cleaned + standardized data (Alberta only, consistent dates).  
- **Gold Layer:** Aggregated data with calculated **Affordability Index**.  

### Tools & Tech
- **Databricks** (free edition, community edition for development)  
- **PySpark** for distributed data processing  
- **Delta Lake** for versioned tables (Bronze/Silver/Gold)  
- **GitHub** for version control + collaboration  

---

## 📂 Repository Structure
