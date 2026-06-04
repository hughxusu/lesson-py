def self_add(a):
    print(f'a={a}, a_id={id(a)}')
    a += a
    print(f'a={a}, a_id={id(a)}')

b = 100
self_add(b)
print(f'b={b}, b_id={id(b)}')