import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SECRET_TOKEN = os.getenv('SECRET_KEY', "superS3cr3t")
    NUM_PAGES = int(os.getenv('NUM_PAGES', 5))
    PROXY = os.getenv('PROXY')
    CACHE_EXPIRY = int(os.getenv('CACHE_EXPIRY', 3600))
    RETRY_DELAY = int(os.getenv('RETRY_DELAY', 5))

settings = Settings()