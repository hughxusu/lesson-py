def my_generator(n):
    for i in range(n):
        print('start...')
        yield i
        print('end...')
        
g = my_generator(3)

for value in g:
    print(value)