import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, LSTM

# Define the stock symbol and path to the CSV file
symbol = 'AAPL'
csv_path = f'Keras RNN Example/data/{symbol}.csv'

# Load the historical data from the CSV file
data = pd.read_csv(csv_path, index_col='Date', parse_dates=True)

# Scale the data using a MinMaxScaler
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1, 1))

# Define the training data and labels
look_back = 60
train_data = []
labels = []
for i in range(look_back, len(scaled_data)):
    train_data.append(scaled_data[i-look_back:i, 0])
    labels.append(scaled_data[i, 0])
train_data, labels = np.array(train_data), np.array(labels)

# Reshape the data for input into the LSTM
train_data = np.reshape(train_data, (train_data.shape[0], train_data.shape[1], 1))

# Define the LSTM model
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(train_data.shape[1], 1)))
model.add(LSTM(units=50))
model.add(Dense(units=1))

# Compile and train the model
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(train_data, labels, epochs=10, batch_size=32)

# Use the trained model to predict future stock prices
test_data = scaled_data[-look_back:]
test_data = np.reshape(test_data, (1, test_data.shape[0], 1))
predicted_prices = []
for i in range(30):
    prediction = model.predict(test_data)
    predicted_prices.append(prediction[0, 0])
    test_data = np.append(test_data[:, 1:, :], prediction.reshape(1, 1, -1), axis=1)

# Reverse the scaling of the predicted prices
predicted_prices = scaler.inverse_transform(np.array(predicted_prices).reshape(-1, 1))

# Plot the predicted prices against the actual prices
plt.plot(data[-30:].index.values, data[-30:]['Close'].values, label='Actual Price')
plt.plot(data[-30:].index.values, predicted_prices, label='Predicted Price')
plt.title(f'{symbol} Closing Price Prediction')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
