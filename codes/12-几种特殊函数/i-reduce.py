import functools

arr = [1, 2, 3, 4]

def sum(a, b):
    return a + b

result = functools.reduce(sum, arr)

print(result)