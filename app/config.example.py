from pydantic import BaseSettings
from dotenv import load_dotenv
import os
import logging

load_dotenv()


class Settings(BaseSettings):
    app_name: str = "Trading View Bot"
    admin_email: str = ""
    TELEGRAM_TOKEN: str = ""
    # Create a Telegram group. Add bot to this group. Say /my_id @botname
    # https://api.telegram.org/bot1792:3ew0/getUpdates
    CHAT_ID: str = ""
    LOG_FORMAT = "%(levelname)s %(filename)s line:%(lineno)d %(asctime)s - %(message)s"
    logging.basicConfig(filename="logs/admin.log", level=logging.INFO, format=LOG_FORMAT)
    class Config:
        env_file = "../.env"

    
class TestSettings(Settings):
    # Test your bot before playing with real money: https://testnet.binance.vision
    BINANCE_API_KEY: str = ""
    BINANCE_API_SECRET: str = ""
    TEST_API_URL: str = "https://testnet.binance.vision/api"


class ProdSettings(Settings):
    BINANCE_API_KEY: str = ""
    BINANCE_API_SECRET: str = ""


# Set it TestSettings() or ProdSettings()
settings = TestSettings()
