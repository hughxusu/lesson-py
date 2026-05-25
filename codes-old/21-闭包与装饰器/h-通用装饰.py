def count_calls(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{func.__name__} 函数调用 {count} 次:", end='\t')
        return func(*args, **kwargs)
    return wrapper

@count_calls
def greet(first, last):
    return f"Hello, {first.title()} {last.title()}"

print(greet("john", "doe"))
print(greet("alice", "smith"))
