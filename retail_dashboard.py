# retail_dashboard_updated.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Streamlit page config
st.set_page_config(
    page_title="Retail Sales Analytics Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 Retail Sales Analytics Dashboard")

# --- Sidebar for file upload and filters ---
st.sidebar.header("Upload your sales data")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    # Load data
    df = pd.read_csv(uploaded_file)
    
    st.sidebar.header("Filter Data")
    # Filter by date
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
        start_date = st.sidebar.date_input("Start Date", df['Date'].min())
        end_date = st.sidebar.date_input("End Date", df['Date'].max())
        df = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]

    # Filter by region if exists
    if 'Region' in df.columns:
        regions = st.sidebar.multiselect("Select Region", df['Region'].unique(), default=df['Region'].unique())
        df = df[df['Region'].isin(regions)]

    # --- Main KPIs ---
    st.subheader("Key Performance Indicators (KPIs)")
    col1, col2, col3 = st.columns(3)

    total_sales = df['Sales'].sum() if 'Sales' in df.columns else 0
    total_orders = df['OrderID'].nunique() if 'OrderID' in df.columns else 0
    total_profit = df['Profit'].sum() if 'Profit' in df.columns else 0

    col1.metric("Total Sales", f"${total_sales:,.2f}")
    col2.metric("Total Orders", total_orders)
    col3.metric("Total Profit", f"${total_profit:,.2f}")

    # --- Sales Over Time ---
    st.subheader("Sales Over Time")
    if 'Date' in df.columns and 'Sales' in df.columns:
        sales_over_time = df.groupby('Date')['Sales'].sum().reset_index()
        plt.figure(figsize=(12,4))
        sns.lineplot(data=sales_over_time, x='Date', y='Sales', marker='o')
        plt.xticks(rotation=45)
        plt.ylabel("Sales ($)")
        plt.tight_layout()
        st.pyplot(plt)

    # --- Top Products ---
    st.subheader("Top 10 Products by Sales")
    if 'Product' in df.columns and 'Sales' in df.columns:
        top_products = df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(10).reset_index()
        plt.figure(figsize=(10,6))
        sns.barplot(data=top_products, x='Sales', y='Product', palette='viridis')
        plt.xlabel("Sales ($)")
        plt.ylabel("Product")
        st.pyplot(plt)

    # --- Sales by Region ---
    st.subheader("Sales by Region")
    if 'Region' in df.columns and 'Sales' in df.columns:
        sales_by_region = df.groupby('Region')['Sales'].sum().reset_index()
        plt.figure(figsize=(8,5))
        sns.barplot(data=sales_by_region, x='Region', y='Sales', palette='magma')
        plt.ylabel("Sales ($)")
        plt.xlabel("Region")
        st.pyplot(plt)

else:
    st.info("Please upload a CSV file to get started.")