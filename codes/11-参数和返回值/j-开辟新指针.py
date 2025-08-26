a = 1
b = a

print(f'a={a}, b={b}')
print(f'a_id={id(a)}, b_id={id(b)}')

a = 2
print(f'a={a}, b={b}')
print(f'a_id={id(a)}, b_id={id(b)}')