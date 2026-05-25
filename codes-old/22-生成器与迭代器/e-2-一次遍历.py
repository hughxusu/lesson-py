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


fib_iter = FibonacciIterator(10)
result = []
for num in fib_iter:
    result.append(num)
print(f'result 结果为: {result}')

for num in fib_iter:
    print(f'当前元素为: {num}')
