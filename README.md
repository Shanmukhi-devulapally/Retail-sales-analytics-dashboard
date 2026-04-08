# 📊 Retail Sales Analytics Dashboard

A powerful and interactive **data visualization dashboard** built using **Streamlit**, designed to analyze retail sales data from a CSV file. This app provides key insights such as sales trends, top-performing products, and regional performance.

---

## 📌 Features

* 📂 Upload your own retail sales CSV file
* 📅 Filter data by date range
* 🌍 Filter sales by region
* 📈 View Key Performance Indicators (KPIs):

  * Total Sales
  * Total Orders
  * Total Profit
* 📊 Visualizations:

  * Sales over time (line chart)
  * Top 10 products by sales (bar chart)
  * Sales by region (bar chart)
* 🖥️ Wide layout for better dashboard experience

---

## 📁 Expected Dataset Format

Your CSV file should include some or all of the following columns:

* `Date` – Order or transaction date
* `Sales` – Sales amount
* `Profit` – Profit earned
* `OrderID` – Unique order identifier
* `Product` – Product name
* `Region` – Sales region

> ⚠️ The app handles missing columns gracefully, but more complete data gives better insights.

---

## 🚀 How to Run the Project

### 1. Install Required Libraries

```bash
pip install streamlit pandas matplotlib seaborn
```

---

### 2. Save the File

```bash
retail_dashboard_updated.py
```

---

### 3. Run the App

```bash
streamlit run retail_dashboard_updated.py
```

---

## 🖥️ How to Use

1. Launch the app in your browser
2. Upload your CSV file using the sidebar
3. Apply filters:

   * Select date range
   * Choose regions
4. Explore:

   * KPI metrics at the top
   * Sales trends over time
   * Best-selling products
   * Regional sales distribution

---

## 📊 Dashboard Sections

### 🔹 Key Performance Indicators (KPIs)

Quick summary of:

* Total Sales ($)
* Total Orders
* Total Profit ($)

---

### 🔹 Sales Over Time

* Line chart showing how sales change across dates
* Helps identify trends and seasonality

---

### 🔹 Top Products

* Displays top 10 products based on total sales
* Useful for inventory and marketing decisions

---

### 🔹 Sales by Region

* Compares sales performance across regions
* Helps identify high-performing areas

---

## ⚠️ Notes

* Ensure your CSV file uses correct column names (case-sensitive)
* Date column should be in a recognizable date format
* Large datasets may take time to load

---

## 💡 Future Improvements

* Add profit analysis charts
* Include customer segmentation
* Export dashboard reports
* Add interactive filters for products/categories
* Use Plotly for more interactive charts

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* Matplotlib
* Seaborn

---

## 👨‍💻 Author

Devulapally Shanmukhi

---

## 📌 Conclusion

This dashboard is a great starting point for **data analysis and business intelligence projects**, helping users quickly gain insights from raw retail data.

---

✨ Feel free to customize and expand it based on your needs!
# Retail-sales-analytics-dashboard
