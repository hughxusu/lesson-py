def self_add(a):
    print(f'a={a}, a_id={id(a)}')
    a += a
    print(f'a={a}, a_id={id(a)}')

c = [11, 22]
self_add(c)
print(f'c={c}, a_id={id(c)}')
