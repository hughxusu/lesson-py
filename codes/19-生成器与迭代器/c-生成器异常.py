def my_generator(n):
    for i in range(n):
        print('start...')
        yield i
        print('end...')
        
g = my_generator(3)
while True:
    try:
        result = next(g)
        print(result)
    except StopIteration as e:
        break