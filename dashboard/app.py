import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath("."))

from backend.ai_service import ask_ai_about_data

st.title("AI Dashboard Assistant")

df = pd.read_csv("data/sample_sales.csv")

st.subheader("Sales Data")
st.dataframe(df)

st.subheader("Revenue by Product")
st.bar_chart(df.set_index("product_name")["revenue"])

st.subheader("Ask AI About Your Data")

user_question = st.text_input(
    "Example: Which product generated the most revenue?"
)

if user_question:
    data_summary = df.to_string(index=False)

    with st.spinner("AI is analyzing your data..."):
        answer = ask_ai_about_data(user_question, data_summary)

    st.success(answer)