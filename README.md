# Retail Sales & Analytics Dashboard 🚀🌟

A retail sales analytics project built using **Python, Streamlit, Pandas, and Plotly**. This dashboard provides insights into sales performance, revenue distribution, product categories, payment methods, and sales channels through interactive visualizations.

## Dashboard Preview

![Retail Sales Analytics Dashboard](screenshots/dashboard-preview.png)

## Project Overview

The Retail Sales & Analytics Dashboard helps analyze retail sales data and understand business performance through key metrics and visual representations.

### Key Performance Indicators (KPIs)

- **Total Revenue:** Overall revenue generated from sales.
- **Total Orders:** Total number of orders placed.
- **Average Order Value:** Average revenue generated per order.
- **Units Sold:** Total number of products sold.

### Data Visualizations

The dashboard includes the following visualizations:

1. Revenue by Product Category
2. Top 10 Best-Selling Items
3. Revenue by Payment Method
4. Revenue by Location Channel

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming and data processing |
| Streamlit | Interactive dashboard development |
| Pandas | Data cleaning and manipulation |
| Plotly Express | Data visualization |
| Jupyter Notebook | Data analysis and exploration |

## Project Structure

```text
DATA_SCIENCE/
│
├── assets/
│
├── dashboards/
│   ├── category_revenue
│   ├── monthly_revenue_trend
│   ├── payment_method_distribution
│   ├── revenue_by_location
│   └── top_items
│
├── data/
│   ├── Cleaned_dataset.csv
│   └── retail_store_sales.csv
│
├── notebooks/
│   ├── Cleaned_dataset.ipynb
│   └── Data_Visualization.ipynb
│
├── screenshots/
│   ├── dashboard-preview.png
│   └── visualization-files.png
│
├── app.py
├── requirements.txt
└── README.md
```

## Visualization Files

The project also contains individual visualizations generated during the data analysis process.

![Visualization Files](screenshots/visualization-files.png)

## Installation and Setup

Follow these steps to run the project on your local machine.

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate to the project directory:

```bash
cd DATA_SCIENCE
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit Application

```bash
streamlit run app.py
```

The dashboard will open in your default web browser. If it does not, open the local URL displayed in the terminal.

## Dataset

The project uses retail sales data stored in CSV format.

- `retail_store_sales.csv` – Original retail sales dataset.
- `Cleaned_dataset.csv` – Processed dataset used for analysis and dashboard visualization.

## Project Objectives

- Perform data cleaning and preprocessing.
- Explore retail sales data using Python.
- Analyze revenue and product performance.
- Understand customer payment preferences.
- Compare sales performance across different channels.
- Present business insights through interactive dashboards.

## Future Improvements

- Add more interactive filters.
- Include monthly and yearly sales trends.
- Add customer segmentation analysis.
- Improve dashboard functionality and design.

## Author

**Sreyasi Das**

BCA Student | Data Analytics & Data Science

GitHub: [Sreyasi27](https://github.com/Sreyasi27)

---

*This project was developed as part of my learning journey in Data Analytics and Data Science.*
