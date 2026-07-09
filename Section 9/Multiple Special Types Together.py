from datetime import datetime
from uuid import UUID

from pydantic import (
    BaseModel,
    EmailStr,
    HttpUrl,
    SecretStr
)


class UserAccount(BaseModel):
    user_id: UUID
    email: EmailStr
    website: HttpUrl
    password: SecretStr
    created_at: datetime


user = UserAccount(
    user_id="550e8400-e29b-41d4-a716-446655440000",
    email="rahul@example.com",
    website="https://example.com",
    password="secret123",
    created_at="2026-07-09T12:30:00"
)


print(user)


# This model combines UUID, email, URL, secret value, and datetime validation in one structured model.