"""Settings"""
from dotenv import load_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):  # pylint: disable=too-few-public-methods
    """Setting Class"""
    api_id: int
    api_hash: str
    openai_key: str


load_dotenv(".env")

settings = Settings()
