def count_calls(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{func.__name__} has been called {count} times")
        return func(*args, **kwargs)
    return wrapper

@count_calls
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

print(fib(5))
print(fib(3))