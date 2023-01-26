import os
from dotenv import load_dotenv


load_dotenv(dotenv_path=".env")

class Settings:
    SQLALCHEMY_DATABASE_URL = os.environ.get("SQLALCHEMY_DATABASE_URL")
    
settings = Settings()