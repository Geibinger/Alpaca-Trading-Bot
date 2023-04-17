import yfinance as yf
import pandas as pd

# Define the stock symbol and date range
symbol = 'AAPL'
start_date = '2022-01-01'
end_date = '2023-04-16'

# Fetch the historical data from Yahoo Finance
data = yf.download(symbol, start=start_date, end=end_date)

# Write the data to a CSV file
data.to_csv(f'Keras RNN Example/data/{symbol}.csv')
