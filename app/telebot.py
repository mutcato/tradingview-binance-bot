# -*- coding: utf-8 -*-
import logging

import telegram

import settings

bot = telegram.Bot(token=settings.TELEGRAM_TOKEN)


def say_hello():
    bot_welcome = """
    Welcome to coolAvatar bot, the bot is using the service from http://avatars.adorable.io/ to generate cool looking avatars based on the name you enter so please enter a name and the bot will reply with an avatar for your name.
    """
    # send the welcoming message
    bot.sendMessage(chat_id=settings.CHAT_ID, text=bot_welcome)

say_hello()