import streamlit as st
import pandas as pd
import yfinance as yf

st.title("Stock Market Analysis")

start_date = st.date_input("Start date", pd.to_datetime("2020-01-01"))
end_date = st.date_input("End date", pd.to_datetime("2023-01-01"))

symbol = "AAPL"
ticker = yf.Ticker(symbol)
ticker_df = ticker.history(start=start_date, end=end_date)

st.dataframe(ticker_df)
st.write("## Closing Price")
st.line_chart(ticker_df["Close"])

col1, col2 = st.columns(2)
with col1:
    st.write("## Daily closing price chart")
    st.line_chart(ticker_df["Close"])  # Fixed typo and case sensitivity
with col2:
    st.write("## Daily volume price chart")
    st.line_chart(ticker_df["Volume"])  # Fixed typo and case sensitivity