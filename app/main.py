# app.py
from functools import lru_cache
from typing import Dict

import uvicorn
from fastapi import FastAPI

from config import settings


from telebot import Telegram

bott = Telegram(**dict(settings))

app = FastAPI()

@app.get('/')
def home():
    return {'hello': 'world'}

@app.post('/notify')
def notify(json_data: Dict):
    action = json_data.get("action")
    coin = json_data.get("coin")
    currency = json_data.get("currency")
    amount = json_data.get("amount")
    bott.send_message(action=action, coin=coin, currency=currency, amount=amount)
    return 

if __name__ == '__main__':
    uvicorn.run(app)
