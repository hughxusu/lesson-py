def print_args(*args):
    print(type(args))
    print(args)

print_args(1, [1, 2], 'red')
print_args([1, 2])