from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='./.env', env_file_encoding='utf-8', extra='allow')

    POSTGRES_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_HOSTNAME: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    SQLALCHEMY_DATABASE_URL: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra='allow')
    db: PostgresSettings = PostgresSettings()


settings = Settings(_env_file='./.env', _env_file_encoding='utf-8')
