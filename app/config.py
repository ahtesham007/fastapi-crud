from pydantic import BaseSettings

class Settings(BaseSettings):
    user: str
    pwd: str
    host: str
    port: int
    db: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int


    class Config:
        env_file = '.env'

settings = Settings()