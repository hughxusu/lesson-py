def all_args(first, second='yellow', *args, **kwargs):
    print(f'first: {first}')
    print(f'second: {second}')
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')

all_args('red', a=1, b=2, c=3)
all_args('red', 'blue', 'white', 'pink', a=1, b=2, c=3)