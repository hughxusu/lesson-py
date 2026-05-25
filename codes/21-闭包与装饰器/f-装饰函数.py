def count_calls(func):
    count = 0
    def wrapper(name):
        nonlocal count
        count += 1
        print(f"{func.__name__} 函数调用 {count} 次:", end='\t')
        func(name)
    return wrapper	

@count_calls
def greet(name):
    print(f"Hello, {name}")

greet("Alice")
greet("Bob")