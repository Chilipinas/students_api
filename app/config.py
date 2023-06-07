from pydantic import BaseSettings

class Settings(BaseSettings):
    db_user: str
    db_password: str
    db_host: str
    db_port: str
    db_name: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()