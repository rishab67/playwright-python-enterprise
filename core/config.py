import os
from dotenv import load_dotenv


# This tells python to find the .env file and unlock it.
load_dotenv()

class Config:
    # We safely grab the secrets. If they don't exist, we throw an error!
    API_BASE_URL = os.getenv("API_BASE_URL")
    UI_BASE_URL = os.getenv("UI_BASE_URL")
    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")