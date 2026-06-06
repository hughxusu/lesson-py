def fibonacci(num):
    a = 0
    b = 1
    
    current_index = 0
    while current_index < num:
        result = a
        a, b = b, a + b
        current_index += 1
        yield result

fib = fibonacci(10)
result = []
for value in fib:
    result.append(value)
print(result)
