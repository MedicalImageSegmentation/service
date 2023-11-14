import os

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Config(BaseSettings):
    DATABASE_SOURCE = os.getenv("database.source")
    DATABASE_POOL_TIMEOUT = os.getenv("database.pool_timeout")
    DATABASE_CONNECT_TIMEOUT = os.getenv("database.connect_timeout")
    DATABASE_POOL_RECYCLE = os.getenv("database.pool_recycle")
    DATABASE_POOL_SIZE = os.getenv("database.pool_size")

    OSS_ENDPOINT = os.getenv("oss.endpoint")
    OSS_ACCESS_KEY = os.getenv("oss.access_key")
    OSS_SECRET_KEY = os.getenv("oss.secret_key")

    JWT_SECRET_KEY = os.getenv("jwt.secret_key")
    JWT_EXPIRATION_TIME = os.getenv("jwt.expiration_time")


settings = Config()
