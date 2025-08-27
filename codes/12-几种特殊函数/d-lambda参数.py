# 无参数
fn = lambda: 100
print(fn())

# 必要参数
fn = lambda top, bottom, h: (top + bottom) * h / 2
print(fn(3, 5, 4))

# 关键字参数
fn = lambda top, bottom, h: (top + bottom) * h / 2
print(fn(3, h=4, bottom=5))

# 默认参数
fn = lambda top, bottom, h=1: (top + bottom) * h / 2
print(fn(3, 5))

# 可变参数
fn = lambda *args, **kwargs: [args, kwargs]
print(fn(1, 2, 3, name='Bob', age=25, job='Dev'))