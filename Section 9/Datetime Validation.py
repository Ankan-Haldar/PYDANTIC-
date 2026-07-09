from datetime import datetime
from pydantic import BaseModel


class Event(BaseModel):
    title: str
    start_time: datetime


event = Event(
    title="Python Workshop",
    start_time="2026-07-09T10:30:00"
)

print(event)
print(type(event.start_time))


# Pydantic converts the valid datetime string into a Python datetime object.