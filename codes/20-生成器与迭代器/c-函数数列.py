def fibonacci(num):
    a = 0
    b = 1
    for _ in range(num):
        a, b = b, a + b

    return a

result = []
for num in range(10):
    result.append(fibonacci(num))


