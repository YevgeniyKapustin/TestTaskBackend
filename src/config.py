from pydantic_settings import BaseSettings


class Config(BaseSettings):
    """Конфиг приложения."""
    APP_NAME: str = 'Тестовое на backend'
    APP_VERSION: str = '1.0'

    # Database
    SQLITE_DSN: str = 'sqlite+aiosqlite:///main.db'

    # JWT Token
    TOKEN_URL: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    JWT_ALGORITHM: str

    class Config:
        env_file = '../.env'
        env_file_encoding = 'utf-8'


config = Config()
