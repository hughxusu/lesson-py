import time

def fibonacci(num):
    a = 0
    b = 1
    
    current_index = 0
    while current_index < num:
        result = a
        a, b = b, a + b
        current_index += 1
        yield result

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@time_it
def def_fibonacci(num):
    fib = fibonacci(num)
    result = []
    for value in fib:
        result.append(value)

def_fibonacci(5000)
