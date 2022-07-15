import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(env_path)


class Settings(object):
    PROJECT_TITLE: str = "Jobboard"
    PROJECT_VERSION: str = "0.1.1"

    PG_USER = os.getenv("POSTGRES_USER")
    PG_PWD = os.getenv("POSTGRES_PASSWORD")
    PG_HOST = os.getenv("POSTGRES_HOST", "localhost")
    PG_PORT = os.getenv("POSTGRES_PORT", 5432)
    PG_DB = os.getenv("POSTGRES_DATABASE")
    DATABASE_URL = f"postgresql://{PG_USER}:{PG_PWD}@{PG_HOST}:{PG_PORT}/{PG_DB}"


settings = Settings()
