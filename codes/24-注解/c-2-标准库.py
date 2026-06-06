from datetime import datetime
from enum import Enum

now: datetime = datetime.now()
print(now)

class Status(Enum):
    OPEN = 1
    CLOSED = 2

status: Status = Status.OPEN
print(status)
