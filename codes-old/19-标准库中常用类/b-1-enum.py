from enum import Enum, auto

class Status(Enum):
    PENDING = auto()
    RUNNING = auto()
    SUCCESS = auto()
    FAILED = auto()

status = Status.PENDING
print(status)
print(f'状态值是: {status.value}, 状态名称是: {status.name}')

status = Status.RUNNING
print(f'状态值是: {status.value}, 状态名称是: {status.name}')
