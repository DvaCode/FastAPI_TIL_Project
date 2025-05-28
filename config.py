from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    database_username: str
    database_password: str
    jwt_secret: str

@lru_cache # 페이지 교체 알고리즘 중 하나 LRU(least recently used) Algorithm
def get_settings():
    return Settings()