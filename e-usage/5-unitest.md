# 软件测试

软件测试金字塔模型

<img src="https://raw.githubusercontent.com/hughxusu/lesson-py/developing/_images/libs/end-to-end-testing-pyramid.webp" style="zoom:60%;" />

## Python单元测试框架

Unitest是Python自带的单元测试工具。

```python
import unittest

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):   # 所有test运行前运行一次
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):  # 所有test运行后运行一次
        print("tearDownClass")

    def setUp(self):  # 每个test运行前运行一次
        print("setUp")

    def tearDown(self):  # 每个test运行后运行一次
        print("tearDown")

    def test_01(self):  # 测试用例
        print('test_01')

    def test_02(self):
        print('test_01')


if __name__ == '__main__':
    unittest.main()
```

Unitest中的断言

断言是用于判断程序是否为预期的结果

| 方法                                                         | 检查对象           |
| :----------------------------------------------------------- | :----------------- |
| [`assertEqual(a, b)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertEqual) | `a == b`           |
| [`assertNotEqual(a, b)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertNotEqual) | `a != b`           |
| [`assertTrue(x)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertTrue) | `bool(x) is True`  |
| [`assertFalse(x)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertFalse) | `bool(x) is False` |

```python
class MyTestCase(unittest.TestCase):
    def test_01(self): 
        a = 10
        b = 10
        self.assertEqual(a, b)
        self.assertNotEquals(a, b)

    def test_02(self):
        c = False
        self.assertFalse(c)
        self.assertTrue(c)
```



