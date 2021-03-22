# app.py
from functools import lru_cache
from typing import Dict

import uvicorn
from fastapi import FastAPI

from config import settings

from binance_trade import Binance
from telebot import Telegram

notifier = Telegram(**dict(settings))
trader = Binance()

app = FastAPI()

@app.get('/')
def home():
    return {'hello': 'world'}

@app.post('/notify')
def notify(json_data: Dict):
    if trader.sell_market():
        notifier.send_message(**json_data)
    else:
        print("Olmadı")
    return 

if __name__ == '__main__':
    uvicorn.run(app)
