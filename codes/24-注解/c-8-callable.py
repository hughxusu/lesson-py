from math import sin
from typing import Callable

type Number = int | float

def add(x: Number, y: Number, f: Callable[[Number], float]) -> float:
    return f(x) + f(y)

print(add(-5, 6, abs))
print(add(-5, 6, sin))