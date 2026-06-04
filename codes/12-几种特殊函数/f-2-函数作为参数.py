from math import sin

def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))
print(add(-5, 6, sin))