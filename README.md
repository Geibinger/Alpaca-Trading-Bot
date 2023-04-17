# Alpaca Trade Example
This Python script uses the Alpaca API to place a market order to buy 100 shares of NVDA stock.

## Prerequisites
Before running this script, you will need:

- An Alpaca account (you can sign up [here](https://app.alpaca.markets/brokerage/dashboard/overview))
- An API key and secret for Alpaca (you can create them [here](https://app.alpaca.markets/brokerage/dashboard/overview))
- The `alpaca_trade_api` Python package installed (you can install it via pip `install alpaca-trade-api`)
## Setup
1) Clone this repository to your local machine.
2) Create a new file named `keys.json` in the same directory as the script.
3) Open the `keys.json` file and paste the following JSON object, replacing `YOUR_API_KEY` and `YOUR_SECRET_KEY` with your own keys:

```json
{
    "Papertrading": {
        "key": "YOUR_API_KEY",
        "secret": "YOUR_SECRET_KEY"
    }
}
```

4) Save and close the `keys.json` file.

## Usage
1) Run the script using python `buy_nvda.py`.
2) The script will attempt to place a market order to buy 100 shares of NVDA stock.
3) If the order is successful, the script will print `Market order placed`. to the console.
4) If the order is unsuccessful, the script will raise an exception with an error message.

## Paper Trading
Alpaca offers a paper trading environment that allows you to test your trading strategies without risking real money. To use paper trading with the Alpaca API:

1) Sign up for a paper trading account [here](https://app.alpaca.markets/brokerage/dashboard/overview).
2) Create a new API key and secret [here](https://app.alpaca.markets/brokerage/dashboard/overview).
3) Use the paper trading API endpoint (`https://paper-api.alpaca.markets`) instead of the live trading endpoint (`https://api.alpaca.markets`) when creating an instance of the `REST` object:

```python
api = tradeapi.REST(API_KEY, SECRET_KEY, 'https://paper-api.alpaca.markets')
```

4) When submitting an order, set the `symbol`, `qty`, `side`, `type`, and `time_in_force` parameters according to your desired trade.

Note: Paper trading orders are executed in a simulated environment and do not affect your real trading account or the stock market.