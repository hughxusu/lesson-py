def count_calls(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{func.__name__} has been called {count} times")
        func(*args, **kwargs)
    return wrapper

@count_calls
def greet(first, last):
    print(f"Hello, {first.title()} {last.title()}")

greet("john", "doe")
greet("alice", "smith")