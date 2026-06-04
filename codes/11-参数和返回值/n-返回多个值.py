def circle(r):
    pi = 3.14
    length = 2 * pi * r
    area = pi * r ** 2
    return length, area

length, area = circle(5)

print(f'length={length}')
print(f'area={area}')
