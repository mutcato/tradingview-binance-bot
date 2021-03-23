from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    app_name: str = "Trading View Bot"
    admin_email: str = ""
    TELEGRAM_TOKEN: str = ""
    # Create a Telegram group. Add bot to this group. Say /my_id @botname
    # https://api.telegram.org/bot1792:3ew0/getUpdates
    CHAT_ID: str = ""

    class Config:
        env_file = "../.env"

    
class TestSettings(Settings):
    # Test your bot before playing with real money: https://testnet.binance.vision
    BINANCE_API_KEY: str = ""
    BINANCE_API_SECRET: str = ""
    TEST_API_URL: str = "https://testnet.binance.vision/api"


class ProdSettings(Settings):
    # Test your bot before playing with real money: https://testnet.binance.vision
    BINANCE_API_KEY: str = ""
    BINANCE_API_SECRET: str = ""


# Set it TestSettings() or ProdSettings
settings = TestSettings()
