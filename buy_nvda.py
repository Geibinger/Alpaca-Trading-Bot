import json
import alpaca_trade_api as tradeapi

# read API keys from the JSON file
with open('keys.json', 'r') as f:
    keys = json.load(f)['Papertrading']

# create an instance of the Alpaca API client
api = tradeapi.REST(keys['key'], keys['secret'], 'https://paper-api.alpaca.markets')

# get account information
account = api.get_account()

# check if the account is restricted from trading
if account.trading_blocked:
    print('Account is currently restricted from trading.')
else:
    # place a market order to buy 100 share of NVDA
    api.submit_order(
        symbol='NVDA',
        qty=100,
        side='buy', # or 'sell'
        type='market',
        time_in_force='gtc'
    )
    print('Market order placed.')
