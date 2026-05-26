import streamlit as st 
import pandas as pd

st.title("AI Dashboard Assistant")

df = pd.read_csv("data/sample_sales.csv")

st.subheader("Sales Data")
st.dataframe(df)

st.bar_chart(df.set_index("product_name")["revenue"])