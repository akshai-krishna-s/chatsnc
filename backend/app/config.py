from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_username: str
    database_name: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    openai_api_key: str
    app: str

    class Config:
        env_file = ".env"


settings = Settings()  # type: ignore
