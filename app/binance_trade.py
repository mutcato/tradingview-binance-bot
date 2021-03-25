from config import settings, logging

from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException


logger = logging.getLogger(__name__)


class Binance:
    def __init__(self, **kwargs):
        self.client = Client(kwargs["BINANCE_API_KEY"], kwargs["BINANCE_API_SECRET"])
        try:
            self.client.API_URL = settings.TEST_API_URL
        except:
            logger.info("Production does not override API_URL", self.client.API_URL)    

    def show_info(self):
        logger.info("Looked general info")
        return self.client.get_account()

    def show_asset_info(self, asset):
        logger.info(f"Looked {asset} info")
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
            logger.error(f"Error on limit_order 'API Exception' {e}")
        except BinanceOrderException as e:
            logger.error(f"Error on limit_order 'Order Exception' {e}")

    def market_order(self, ticker, action, amount):
        try:
            buy_limit = self.client.create_order(
                symbol=ticker,
                side=action, # BUY or SELL
                type="MARKET",
                quantity=amount)
                
            return buy_limit

        except BinanceAPIException as e:
            logger.error(f"Error on market_order 'API Exception' {e}")
        except BinanceOrderException as e:
            logger.error(f"Error on market_order 'Order Exception' {e}")


        
