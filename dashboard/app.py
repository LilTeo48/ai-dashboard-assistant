import streamlit as st
import pandas as pd
import sys
import os
import requests
import plotly.express as px 

sys.path.append(os.path.abspath("."))

from backend.ai_service import ask_ai_about_data
from backend.db_utils import save_sales_to_db, load_sales_from_db

st.set_page_config(
    page_title="AI Dashboard Assistant",
    page_icon="📊",
    layout="wide"
)

st.title("AI Dashboard Assistant")

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

def load_sales_from_api():
    response = requests.get(f"{API_BASE_URL}/sales")
    response.raise_for_status()
    return pd.DataFrame(response.json())

def load_top_products_from_api():
    response = requests.get(f"{API_BASE_URL}/sales/top-products")
    response.raise_for_status()
    return pd.DataFrame(response.json()) 

def load_sales_summary_from_api():
    response = requests.get(f"{API_BASE_URL}/sales/summary")
    response.raise_for_status()
    return response.json()    

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

st.sidebar.header("Database Actions")

if st.sidebar.button("Save Data to PostgreSQL"):
    try:
        saved_count, skipped_count = save_sales_to_db(df)

        st.sidebar.success(
            f"Saved {saved_count} new rows. Skipped {skipped_count} duplicates."
        )

    except Exception as e:
        st.sidebar.error(f"Database save failed: {e}")
        
if st.sidebar.button("Load Data from PostgreSQL"):
    try:
        df = load_sales_from_db()
        df["sale_date"] = pd.to_datetime(df["sale_date"], errors="coerce")
        st.sidebar.success("Data loaded from PostgreSQL successfully.")
    except Exception as e:
        st.sidebar.error(f"Database load failed: {e}")

if st.sidebar.button("Load Data from FastAPI"):
    try:
        df = load_sales_from_api()
        df["sale_date"] = pd.to_datetime(df["sale_date"], errors="coerce")
        st.sidebar.success("Data loaded from FastAPI successfully.")
    except Exception as e:
        st.sidebar.error(f"API load failed: {e}")        

st.sidebar.header("Filters")

df["sale_date"] = pd.to_datetime(df["sale_date"], errors="coerce")

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

min_date = df["sale_date"].min().date()
max_date = df["sale_date"].max().date()

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

    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    filtered_df = filtered_df[
        (filtered_df["sale_date"] >= start_date) &
        (filtered_df["sale_date"] <= end_date)
    ]

st.subheader("Key Metrics")

try:
    summary = load_sales_summary_from_api()

    total_revenue = summary["total_revenue"]
    total_quantity = summary["total_quantity_sold"]
    total_records = summary["total_records"]
    unique_products = summary["unique_products"]
    unique_categories = summary["unique_categories"]

    average_revenue = total_revenue / total_records if total_records else 0

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Total Revenue", f"${total_revenue:,.2f}")
    col2.metric("Quantity Sold", f"{total_quantity:,}")
    col3.metric("Average Revenue", f"${average_revenue:,.2f}")
    col4.metric("Products", f"{unique_products}")
    col5.metric("Categories", f"{unique_categories}")

except Exception:

    total_revenue = filtered_df["revenue"].sum()
    total_quantity = filtered_df["quantity_sold"].sum()
    average_revenue = filtered_df["revenue"].mean()

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Revenue", f"${total_revenue:,.2f}")
    col2.metric("Quantity Sold", f"{total_quantity:,}")
    col3.metric("Average Revenue", f"${average_revenue:,.2f}")


st.subheader("Filtered Sales Data")
st.dataframe(filtered_df)

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Data as CSV",
    data=csv,
    file_name="filtered_sales_data.csv",
    mime="text/csv"
)

st.subheader("Revenue by Product")

if not filtered_df.empty:
    revenue_by_product = (
        filtered_df.groupby("product_name", as_index=False)["revenue"].sum()
    )

    product_chart = px.bar(
        revenue_by_product,
        x="product_name",
        y="revenue",
        title="Revenue by Product",
        labels={
            "product_name": "Product",
            "revenue": "Revenue"
        }
    )

    st.plotly_chart(product_chart, use_container_width=True)

    st.subheader("Revenue by Category")

    revenue_by_category = (
        filtered_df.groupby("category", as_index=False)["revenue"].sum()
    )

    category_chart = px.bar(
        revenue_by_category,
        x="category",
        y="revenue",
        title="Revenue by Category",
        labels={
            "category": "Category",
            "revenue": "Revenue"
        }
    )

    st.plotly_chart(category_chart, use_container_width=True)

else:
    st.warning("No data matches your selected filters.")

st.subheader("Top Products Leaderboard")

try:
    top_products_df = load_top_products_from_api()

    if not top_products_df.empty:
        top_products_df = top_products_df.sort_values(
            by="revenue",
            ascending=False
        ).reset_index(drop=True)

        top_products_df["rank"] = top_products_df.index + 1

        top_3 = top_products_df.head(3)

        if len(top_3) >= 3:
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    f"🥇 {top_3.iloc[0]['product_name']}",
                    f"${top_3.iloc[0]['revenue']:,.0f}"
                )

            with col2:
                st.metric(
                    f"🥈 {top_3.iloc[1]['product_name']}",
                    f"${top_3.iloc[1]['revenue']:,.0f}"
                )

            with col3:
                st.metric(
                    f"🥉 {top_3.iloc[2]['product_name']}",
                    f"${top_3.iloc[2]['revenue']:,.0f}"
                )

        top_products_df = top_products_df[
            ["rank", "product_name", "category", "revenue", "quantity_sold"]
        ]

        st.dataframe(top_products_df)

    else:
        st.info("No top product data available.")

except Exception:
    top_products_df = (
        filtered_df.groupby(["product_name", "category"], as_index=False)
        .agg({
            "revenue": "sum",
            "quantity_sold": "sum"
        })
        .sort_values(by="revenue", ascending=False)
        .reset_index(drop=True)
    )

    top_products_df["rank"] = top_products_df.index + 1

    st.dataframe(
        top_products_df[["rank", "product_name", "category", "revenue", "quantity_sold"]]
    )

st.subheader("Ask AI About Your Filtered Data")
# Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.subheader("AI Chat History")

for chat in reversed(st.session_state.chat_history):
    st.markdown(f"**Question:** {chat['question']}")
    st.success(chat["answer"])

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

        st.session_state.chat_history.append({
            "question": user_question,
            "answer": answer
        })

        st.success(answer)