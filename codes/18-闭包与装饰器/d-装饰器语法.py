def count_calls(func):
    count = 0
    def wrapper():
        nonlocal count
        count += 1
        print(f"{func.__name__} has been called {count} times")
        func()
    return wrapper

@count_calls
def greet():
    print(f"Hello, Alice")

greet()
greet()