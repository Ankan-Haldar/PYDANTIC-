from pydantic import BaseModel, HttpUrl


class Profile(BaseModel):
    username: str
    portfolio: HttpUrl


profile = Profile(
    username="rahul123",
    portfolio="https://example.com"
)

print(profile)

# HttpUrl validates the URL structure and accepts valid HTTP or HTTPS URLs.