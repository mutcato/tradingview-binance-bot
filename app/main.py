# app.py
from functools import lru_cache
from typing import Dict

import uvicorn
from fastapi import FastAPI

from config import settings

from binance_trade import Binance
from telebot import Telegram

bot = Telegram(**dict(settings))

app = FastAPI()

@app.get('/')
def home():
    return {'hello': 'world'}

@app.post('/notify')
def notify(json_data: Dict):
    bot.send_message(**json_data)
    return 

if __name__ == '__main__':
    uvicorn.run(app)
