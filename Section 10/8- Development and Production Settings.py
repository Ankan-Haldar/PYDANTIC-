from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    environment: str = "development"
    debug: bool = True
    database_url: str


settings = Settings(
    database_url="sqlite:///development.db"
)


print(settings)


# The same settings structure can be used with different values in development, testing, staging, and production environments.