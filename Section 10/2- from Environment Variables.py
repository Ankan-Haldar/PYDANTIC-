import os

from pydantic_settings import BaseSettings


os.environ["APP_NAME"] = "AI Application"
os.environ["DEBUG"] = "true"
os.environ["PORT"] = "8000"


class Settings(BaseSettings):
    app_name: str
    debug: bool
    port: int


settings = Settings()


print(settings)
print(type(settings.debug))
print(type(settings.port))



# Environment variables are strings, but Pydantic Settings validates and converts them into the declared Python types.