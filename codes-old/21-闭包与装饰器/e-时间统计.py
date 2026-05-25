import time

def time_it(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper


@time_it
def calculate_total():
    total = 0
    for i in range(1000000):
        total += i
    print(f'total = {total}')

calculate_total()
