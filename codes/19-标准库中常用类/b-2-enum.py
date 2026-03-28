from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 'green'
    BLUE = 'blue'

color = Color.RED
print(color)
