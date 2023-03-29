from enum import Enum
from typing import Optional

from pydantic import BaseSettings



class Settings(BaseSettings):
    NAME: str = "sqladmin-poc"

    DATABASE_HOST: str = ""
    DATABASE_PORT: int = 5432
    DATABASE_NAME: str = ""
    DATABASE_USERNAME: str = ""
    DATABASE_PASSWORD: str = ""

settings = Settings()
