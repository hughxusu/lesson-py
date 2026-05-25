def append_value(value, items=[]):
    items.append(value)
    return items

first = append_value('foo')
print(first)
second = append_value('bar')
print(second)
