# app.py
from functools import lru_cache
from typing import Dict

import uvicorn
from fastapi import FastAPI

from config import settings, logging

from binance_trade import Binance
from telebot import Telegram

logger = logging.getLogger(__name__)

notifier = Telegram(**dict(settings))
trader = Binance(**dict(settings))

app = FastAPI()

@app.get("/")
def home():
    return {"hello": "world", "say hi": settings.admin_email}

@app.post("/market_order")
def market_order(json_data: Dict):
    # json_data = {"ticker":"LTCUSDT", "action": "BUY", "amount":0.06, "price":155}
    order_result = trader.market_order(json_data["ticker"], json_data["action"], json_data["amount"])
    # order_result = {'symbol': 'LTCUSDT', 'orderId': 1487076226, 'orderListId': -1, 'clientOrderId': '8Y9hHgc5kGv28MKn1h86Yj', 'transactTime': 1616546780955, 'price': '0.00000000', 'origQty': '0.06000000', 'executedQty': '0.06000000', 'cummulativeQuoteQty': '11.01300000', 'status': 'FILLED', 'timeInForce': 'GTC', 'type': 'MARKET', 'side': 'BUY', 'fills': [{'price': '183.55000000', 'qty': '0.06000000', 'commission': '0.00006000', 'commissionAsset': 'LTC', 'tradeId': 123232612}]}
    logger.info(f"Order result: {order_result}")
    if order_result:
        notifier.send_message(**json_data)

    return 

@app.post("/limit_order")
def limit_order(json_data: Dict):
    # json_data: {"ticker":"LTCUSDT", "action": "BUY", "amount":0.06, "price":155}
    order_result = trader.limit_order(json_data["ticker"], json_data["action"], json_data["amount"], json_data["price"])
    # order_result = 1
    logger.info(f"Order result: {order_result}")

    if order_result:
        notifier.send_message(**json_data)

    return 

@app.get("/binance_info")
def binance_info():
    return trader.show_info()

@app.get("/asset/{asset}")
def binance_info(asset: str):
    return trader.show_asset_info(asset)

if __name__ == '__main__':
    uvicorn.run(app)
