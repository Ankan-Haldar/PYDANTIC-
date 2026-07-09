from datetime import time, timedelta
from pydantic import BaseModel


class Course(BaseModel):
    start_time: time
    duration: timedelta


course = Course(
    start_time="10:30:00",
    duration=7200
)

print(course)


# start_time=datetime.time(10, 30) duration=datetime.timedelta(seconds=7200)