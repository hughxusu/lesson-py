def make_div(func):
    def inner(*args, **kwargs):
        return "<div>" + func(*args, **kwargs) + "</div>"
    return inner

def make_p(func):
    def inner(*args, **kwargs):
        return "<p>" + func(*args, **kwargs) + "</p>"
    return inner

@make_p
@make_div
def greet(name):
    return f"Hello, {name}"

result = greet("Alice")
print(result)