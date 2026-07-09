from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env"
    )

    database_url: str
    debug: bool


settings = Settings()


print(settings.database_url)
print(settings.debug)


# Database configuration is loaded from external settings instead of being written directly in the application code.