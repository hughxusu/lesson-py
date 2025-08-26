# 指向相同的存储空间
a = 1
b = 2
c = 1

print(id(a))
print(id(b))
print(id(c))


# 开辟新的存储空间
a = 280
b = 300
c = 280

print(id(a))
print(id(b))
print(id(c))


# 其它不可变变量
a = 'hello, world'
b = 'hello, world!'
c = 'hello, world'

print(id(a))
print(id(b))
print(id(c))

a = 1, 2
b = 1, 1
c = 1, 2

print(id(a))
print(id(b))
print(id(c))