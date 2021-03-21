from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    app_name: str = "Trading View Bot"
    admin_email: str = ""
    TELEGRAM_TOKEN: str = ""
    CHAT_ID: str = ""

    class Config:
        env_file = "../.env"

settings = Settings()
