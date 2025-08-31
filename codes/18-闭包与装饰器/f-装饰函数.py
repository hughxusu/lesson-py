def count_calls(func):
    count = 0
    def wrapper(name):
        nonlocal count
        count += 1
        print(f"{func.__name__} has been called {count} times")
        func(name)
    return wrapper	

@count_calls
def greet(name):
    print(f"Hello, {name}")

greet("Alice")
greet("Bob")