# C:\projects\vueles\back-vue-sneakers\app\config.py
from typing import Union, List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Sneackers"
    debug: bool = True
    database_url: str = "postgresql://sneackers:sneackers@localhost:5432/sneackers"
    cors_origins: Union[List[str], str] = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
    ]
    static_dir: str = "static"
    images_dir: str = "static/images"

    class Config:
        env_file = ".env"

settings = Settings()
