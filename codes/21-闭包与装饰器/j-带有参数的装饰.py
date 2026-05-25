def make_label(label):
    def decorator(func):
        def inner(*args, **kwargs):
            return f"<{label}>" + func(*args, **kwargs) + f"</{label}>"
        return inner
    return decorator

@make_label('p') # 先调用make_label('p')函数返回装饰器，装饰器与@结合生效。
@make_label('div')
def greet(name):
    return f"Hello, {name}"

result = greet("Alice")
print(result)