def my_generator(n):
    for i in range(n):
        print('start...')
        yield i
        print('end...')
        
g = my_generator(3)
print(g)
print(f'当前元素为: {next(g)}')
print(f'当前元素为: {next(g)}')
print(f'当前元素为: {next(g)}')
# print(next(g))
