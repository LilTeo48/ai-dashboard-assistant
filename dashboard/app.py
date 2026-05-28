import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath("."))

from backend.ai_service import ask_ai_about_data

st.set_page_config(
    page_title="AI Dashboard Assistant",
    page_icon="📊",
    layout="wide"
)

st.title("AI Dashboard Assistant")

st.sidebar.header("Data Source")

uploaded_file = st.sidebar.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.sidebar.success("Uploaded CSV loaded successfully.")
else:
    df = pd.read_csv("data/sample_sales.csv")
    st.sidebar.info("Using default sample sales data.")

required_columns = {"product_name", "category", "quantity_sold", "revenue", "sale_date"}

if not required_columns.issubset(df.columns):
    st.error(
        "CSV must include these columns: product_name, category, quantity_sold, revenue, sale_date"
    )
    st.stop()

df["sale_date"] = pd.to_datetime(df["sale_date"], errors="coerce")

st.sidebar.header("Filters")

categories = sorted(df["category"].dropna().unique())
selected_categories = st.sidebar.multiselect(
    "Filter by Category",
    categories,
    default=categories
)

products = sorted(df["product_name"].dropna().unique())
selected_products = st.sidebar.multiselect(
    "Filter by Product",
    products,
    default=products
)

min_date = df["sale_date"].min()
max_date = df["sale_date"].max()

selected_date_range = st.sidebar.date_input(
    "Filter by Sale Date",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

filtered_df = df[
    (df["category"].isin(selected_categories)) &
    (df["product_name"].isin(selected_products))
]

if len(selected_date_range) == 2:
    start_date, end_date = selected_date_range
    filtered_df = filtered_df[
        (filtered_df["sale_date"] >= pd.to_datetime(start_date)) &
        (filtered_df["sale_date"] <= pd.to_datetime(end_date))
    ]

st.subheader("Key Metrics")

total_revenue = filtered_df["revenue"].sum()
total_quantity = filtered_df["quantity_sold"].sum()
average_revenue = filtered_df["revenue"].mean()

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Quantity Sold", f"{total_quantity:,}")
col3.metric("Average Revenue", f"${average_revenue:,.2f}")

st.subheader("Filtered Sales Data")
st.dataframe(filtered_df)

st.subheader("Revenue by Product")

if not filtered_df.empty:
    revenue_by_product = filtered_df.groupby("product_name")["revenue"].sum()
    st.bar_chart(revenue_by_product)

    st.subheader("Revenue by Category")
    revenue_by_category = filtered_df.groupby("category")["revenue"].sum()
    st.bar_chart(revenue_by_category)
else:
    st.warning("No data matches your selected filters.")

st.subheader("Ask AI About Your Filtered Data")

user_question = st.text_input(
    "Example: Which product generated the most revenue?"
)

if user_question:
    if filtered_df.empty:
        st.warning("No data available for the AI to analyze.")
    else:
        data_summary = filtered_df.to_string(index=False)

        with st.spinner("AI is analyzing your filtered data..."):
            answer = ask_ai_about_data(user_question, data_summary)

        st.success(answer)