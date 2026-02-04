# 📊 Sales Forecasting Dashboard

## 📌 Project Overview
This project demonstrates an end-to-end **Sales Forecasting and Analytics solution** using **Python** for data processing and forecasting, and **Power BI** for interactive dashboard visualization.  
The objective is to analyze historical sales performance and forecast future sales to support data-driven business decisions.

---

## 🛠 Tools & Technologies
- Python (Anaconda, Command Prompt)
- Power BI Desktop
- Pandas, NumPy
- CSV files
- Git & GitHub

> Note: VS Code and Jupyter Notebook were not used. Python scripts were executed via command line.

---

## 📂 Datasets Used

### 1️⃣ Historical Sales Dataset
- File: `data/clean_sales_data.csv`
- Purpose:
  - KPI calculations (Sales, Profit, Quantity)
  - Monthly sales trend analysis
  - Regional and category performance analysis

**Key Columns:**
- Order Date  
- Sales  
- Profit  
- Quantity  
- Region  
- Category  
- Segment  

---

### 2️⃣ Sales Forecast Dataset
- File: `data/sales_forecast.csv`
- Generated using Python forecasting logic
- Used for future sales trend visualization in Power BI

**Key Columns:**
- Month  
- Forecasted_Sales  

---

## 🔄 Project Workflow
1. Load raw sales data
2. Perform data cleaning and transformation using Python (ETL)
3. Generate sales forecasts from historical data
4. Export clean and forecasted datasets as CSV files
5. Build interactive Power BI dashboard

---

## 📈 Power BI Dashboard Features
- Total Sales, Profit, and Quantity KPIs
- Monthly Sales Trend
- Region-wise Sales Comparison
- Category-wise Sales Distribution
- Sales Forecast Visualization
- Interactive filters for user-driven analysis

---

## 📁 Project Structure

Sales_Forecasting_Dashboard/
│
├── data/
│ ├── raw_sales.csv
│ ├── clean_sales_data.csv
│ └── sales_forecast.csv
│
├── scripts/
│ ├── etl_pipeline.py
│ └── sales_forecast_model.py
│
├── Sales_Forecasting_Dashboard.pbix
└── README.md


---

## ▶️ How to Run the Project
1. Navigate to the project directory
2. Run ETL pipeline:


python scripts/etl_pipeline.py

3. Run sales forecasting model:


python scripts/sales_forecast_model.py

4. Open the Power BI file and refresh data

---

## 🎯 Key Learnings
- End-to-end data pipeline development
- Sales trend and performance analysis
- Forecasting business metrics
- Building executive-level Power BI dashboards

---

## 👤 Author
**Sahana D**  
GitHub: https://github.com/sahanad14
