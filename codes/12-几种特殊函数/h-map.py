arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def square(x):
    return x ** 2

result = map(square, arr)

print(type(result))
print(list(result))

# 使用 lambda 函数替代
result = map(lambda x: x ** 2, arr)

print(type(result))
print(list(result))