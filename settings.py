import os
from dotenv import load_dotenv
from pydantic import BaseSettings

class Settings(BaseSettings):
    api_id: int
    api_hash: str
    openai_key: str

if os.path.exists(".env"):
    load_dotenv(".env")

settings = Settings()

