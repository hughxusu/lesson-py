def my_generator(n):
    for i in range(n):
        print('start...')
        yield i
        print('end...')
        
g = my_generator(3)
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))