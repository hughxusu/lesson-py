def append_value(value, items=[]):
    items.append(value)
    return items

first = append_value('foo')
print(f'first={id(first)}')
print(f'__defaults__={id(append_value.__defaults__[0])}') # 读取参数的默认值
