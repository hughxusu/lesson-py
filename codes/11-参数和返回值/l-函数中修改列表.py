def self_add(a):
    print(f'a={a}, a_id={id(a)}')
    a += a
    print(f'a={a}, a_id={id(a)}')

# 1. 不可变类型
b = 100
self_add(b)
print(f'b={b}, b_id={id(b)}')

# 2. 可变类型
c = [11, 22]
self_add(c)
print(f'c={c}, a_id={id(c)}')

# 3. 可变类型，使用切片形式调用
c = [11, 22]
self_add(c[:]) # 使用切片形式调用
print(f'c={c}, a_id={id(c)}')