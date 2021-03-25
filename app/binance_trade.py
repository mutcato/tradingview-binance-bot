from config import settings

from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException


class Binance:
    def __init__(self, **kwargs):
        self.client = Client(kwargs["BINANCE_API_KEY"], kwargs["BINANCE_API_SECRET"])
        try:
            self.client.API_URL = settings.TEST_API_URL
        except:
            print("Production does not override API_URL", self.client.API_URL)    

    def show_info(self):
        return self.client.get_account()

    def show_asset_info(self, asset):
        return self.client.get_asset_balance(asset=asset)

    def limit_order(self, ticker, action, amount, price):
        try:
            buy_limit = self.client.create_order(
                symbol=ticker,
                side=action, # BUY or SELL
                type="LIMIT",
                timeInForce="GTC",
                quantity=amount,
                price=price)

            return buy_limit

        except BinanceAPIException as e:
            # error handling goes here
            print(e)
        except BinanceOrderException as e:
            # error handling goes here
            print(e)

    def market_order(self, ticker, action, amount):
        try:
            buy_limit = self.client.create_order(
                symbol=ticker,
                side=action, # BUY or SELL
                type="MARKET",
                quantity=amount)
                
            return buy_limit

        except BinanceAPIException as e:
            # error handling goes here
            print(e)
        except BinanceOrderException as e:
            # error handling goes here
            print(e)
    def sell_market(self):
        try:
            print("Sell with market price")
            return True
        except Exception as e:
            print(e)

    def buy_market(self):
        print("Buy with market price")

        
