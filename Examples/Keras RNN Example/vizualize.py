import pandas as pd
import matplotlib.pyplot as plt

# Define the stock symbol and path to the CSV file
symbol = 'AAPL'
csv_path = f'Keras RNN Example/data/{symbol}.csv'

# Load the historical data from the CSV file
data = pd.read_csv(csv_path, index_col='Date', parse_dates=True)

# Plot the closing price data in a chart
plt.plot(data['Close'])
plt.title(f'{symbol} Closing Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
