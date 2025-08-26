def print_args(**kwargs):
    print(type(kwargs))
    print(kwargs)

print_args(name='Bob', age=25, job='dev')