my_generator = (i for i in range(3))
print(my_generator)

print(f'当前元素为: {next(my_generator)}')
print(f'当前元素为: {next(my_generator)}')
print(f'当前元素为: {next(my_generator)}')
# print(next(my_generator))