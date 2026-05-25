import time

def fibonacci(num):
    a = 0
    b = 1
    for _ in range(num):
        a, b = b, a + b

    return a

class FibonacciIterator:
    def __init__(self, max_count):
        self.max_count = max_count  
        self.count = 0              
        self.a = 0                  
        self.b = 1                  

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration     

        if self.count == 0:
            self.count += 1
            return self.a          

        if self.count == 1:
            self.count += 1
            return self.b           

        next_value = self.a + self.b
        self.a = self.b
        self.b = next_value
        self.count += 1
        return next_value  


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
    result = []
    for i in range(num):
        result.append(fibonacci(i))

@time_it
def iter_fibonacci(num):
    result = []
    fib_iter = FibonacciIterator(num)
    for i in fib_iter:
        result.append(i)


def_ = def_fibonacci(5000)
iter_ = iter_fibonacci(5000)



