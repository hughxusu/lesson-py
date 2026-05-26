# 类函数重写

## 重写`+`操作符

在 Python 中，可以通过定义特殊方法 `__add__` 来重写 `+` 操作符。这种方法允许你自定义两个对象相加的行为。下面是一个简单的示例，展示了如何在自定义类中重写 `+` 操作符。

假设我们有一个表示二维向量的类 `Vector`，我们希望能够使用 `+` 操作符来实现向量的加法运算。以下是完整的代码示例：

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# 示例使用
v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2  # 使用重载的 + 操作符
print(v3)  # 输出：Vector(4, 6)
```

通过这种方式，可以自定义`+`操作符，使其适用于自定义类，也可以类似地重载其他运算符，例如 `__sub__`（用于 `-` 操作符），`__mul__`（用于 `*` 操作符）等。

