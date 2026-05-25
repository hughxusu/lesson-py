from typing import TypeVar

T = TypeVar('T', str, int)

def add(x: T, y: T) -> T:
    return x + y


print(add('hello', 'world'))
print(add(1, 2))
