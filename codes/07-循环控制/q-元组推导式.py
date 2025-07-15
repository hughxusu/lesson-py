evens = (i for i in range(0, 11, 2))
print(type(evens))
print(evens)

result = tuple(evens)
print(type(result))
print(result)