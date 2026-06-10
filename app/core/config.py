from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Clinic Service API"
    API_V1_PREFIX: str = "/api/v1"

    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    EXTERNAL_HEALTH_FEED_URL: str = "https://disease.sh/v3/covid-19/countries/SL"

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)


settings = Settings()
