def add[T: (str, int)](x: T, y: T) -> T:
    return x + y

print(add('hello', 'world'))
print(add(1, 2))
