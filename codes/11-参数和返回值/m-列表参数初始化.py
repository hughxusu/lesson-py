def append_value(value, items=[]):
    items.append(value)
    return items

first = append_value('foo')
print(first)
second = append_value('bar')
print(second)

# 读取参数的默认值
print(append_value.__defaults__[0])

# def append_value(value, items=None):
#     if items is None:
#         items = []
#     items.append(value)
#     return items