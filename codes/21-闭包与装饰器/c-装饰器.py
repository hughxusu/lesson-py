def count_calls(func):
    count = 0
    def wrapper():
        nonlocal count
        count += 1
        print(f"{func.__name__} 函数调用 {count} 次:", end='\t')
        func()
    return wrapper

def greet():
    print(f"Hello, world")

greet = count_calls(greet)
greet()
greet()