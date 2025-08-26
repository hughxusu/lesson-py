a = [1, 2]
b = [1, 1]
c = [1, 2]

print(id(a))
print(id(b))
print(id(c))

print(id(a[0]) == id(b[0])) # 数组里相同的不可变类型指向相同的地址