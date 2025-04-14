import streamlit as st
import pandas as pd
import numpy as np

import yfinance as yf


st.title('Stock Market Analysis!!')

#st.header('Stock Price Analysis')
#st.subheader('Stock Price Data')
#st.write('This is a simple stock price analysis app using Streamlit and yfinance library.')


# let's see exampls of Widgets
#if st.checkbox('Click me if you want more information'):
#	st.write('This is a checkbox')
#	st.write('This is a radio button')
#	st.write('This is a select box')
#	st.write('This is a multiselect box')
#	st.write('This is a slider')
#	st.write('This is a text input')
#	st.write('This is a number input')
#	st.write('This is a date input')
#	st.write('This is a time input')
#	st.write('This is a file uploader')


start_date = st.date_input('Start date', pd.to_datetime('2020-01-01'))
end_date = st.date_input('End date', pd.to_datetime('2023-01-01'))


#symbol = 'AAPL'
ticker_symbol = st.text_input('Enter the stock ticker symbol', 'AAPL')

ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period = '1d', start=start_date, end=end_date)


st.dataframe(ticker_df)

# let's create some charts

st.write('## Closing Price Chart')
st.line_chart(ticker_df['Close']) # inside line_chart pass the series 

col1, col2 = st.columns(2)

with col1:
	st.write(
		"""
		   ## Daily Closing Price Chart
		"""
	)
	st.line_chart(ticker_df.Close)

with col2:
	st.write(
		"""
		   ## Daily Volume Price Chart
		"""
	)
	st.line_chart(ticker_df.Volume)
