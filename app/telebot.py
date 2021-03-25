# -*- coding: utf-8 -*-
from functools import lru_cache
import logging

import telegram



class Telegram:
    def __init__(self, **kwargs):
        self.token = kwargs["TELEGRAM_TOKEN"]
        self.chat_id = kwargs["CHAT_ID"]
        self.bot = telegram.Bot(token=self.token)

    def say_hello():
        bot_welcome = """
        Welcome
        """
        # send the welcoming message
        self.bot.sendMessage(chat_id=self.chat_id, text=bot_welcome)

    def send_message(self, **kargs):
        # send the welcoming message
        action_past_tense = "BOUGHT" if kargs['action'] == "BUY" else "SOLD"
        message = f"{kargs['amount']} {kargs['currency']} {kargs['ticker']} {action_past_tense} at Price: {kargs['close']}"
        result = self.bot.sendMessage(chat_id=self.chat_id, text=message)
        return result