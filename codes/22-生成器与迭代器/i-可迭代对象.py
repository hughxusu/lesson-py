from collections.abc import Iterable

my_generator = (i for i in range(3))
msg = '插脚红尘已是颠，更求平地上青天。'

print(f'list是否可迭代: {isinstance([1, 2, 3], Iterable)}') 
print(f'generator是否可迭代: {isinstance(my_generator, Iterable)}')
print(f'字符串是否可迭代: {isinstance(msg, Iterable)}')
print(f'整数是否可迭代: {isinstance(123, Iterable)}') 

