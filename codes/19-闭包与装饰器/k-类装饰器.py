class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
        
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} 函数调用 {self.count} 次:", end='\t')
        return self.func(*args, **kwargs)

@CountCalls
def greet(first, last):
    return f"Hello, {first.title()} {last.title()}"

print(greet("john", "doe"))
print(greet("alice", "smith"))
