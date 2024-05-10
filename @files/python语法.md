# 语法基础

## 变量和运算

### 数据类型



##### 字符编码

Unicode是一种所有符号的编码规范，目前Unicode规范是用4个字节来表示一个字符。ASCII规范包含在Unicode中。

UTF-8是 Unicode在计算上的实现方式之一。它的一个特点，就是它是一种变长的编码方式。它可以使用1~4个字节表示一个符号，根据不同的符号而变化字节长度，因此二者的编码值有所不同。

### 运算符

#### `==`和`is`

* `==`是用来判断两个变量的值是否相等
* `is`是用来判断变量是否指向同一个对象
* `is`可以用来判断Ture和False

```python
a = [11, 22, 33]
b = [11, 22, 33]

# 值相等不是同一个对象
a == b # True
a is b # False

# 在一定数据范围内使用相同的内存地址
a = 100
b = 100 
a == b # True
a is b # True
```

### 深拷贝和浅拷贝

```python
a = [11, 22, 33]
b = a

import copy
c = copy.deepcopy(a)

a = [11, 22, 33]
b = [44, 55, 66]
c = [a, b]
d = copy.deepcopy(c) # 如果数据是引用会递归拷贝
d = copy.copy(c) # 只对一层进行深拷贝

c = (a, b)
d = copy.deepcopy(c)
d = copy.copy(c) # 如果拷贝的是不可变类型，则进行浅拷贝
```

## 类

### 定义和使用

```python
class Cat:
  def eat(self):
    print('eatting...')
    
    
tom = Cat()
tom.eat()

tom.name = 'tom' # 动态添加属性
tom.age = 18 

print(tom.name)
```

#### 私有属性和方法

```python
class Dog:
  
  def __init__(self, name):
    self.name = name
    self.__age = 0 # 定义私有属性
    
  def __test(self): # 定义私有方法
    pass
```

#### 内置方法

```python
class Cat:
  def __new__(cls): # 创建对象方法
    print('new---')
    return object.__new__(cls)
  
  def __init__(self, name, age): # 初始化方法
    self.name = name
    self.age = age
    
  def __str__(self):
    return self.name  
  
  def __del__(self):  # 对象删除时调用
    print('over')
    
  def eat(self):
    print('eatting...')
    
    
tom = Cat('tom', 18)
tom.eat()

print(tom.name)
print(tom)  # 会打印__str__的返回值
del tom # 删除对象，调用__del__方法


```

### 继承

```python
class Animal:
  def eat(self):
    print('eat')
    
class Dog(Animal):
  def bark(self):
    print('bark')

class FlyDog(Animal):
  def bark(self): # 重写
    print('super bark')
    Dog.bark(self) # 调用父类方法之一，可以处理多继承问题
    super().bark() # 调用父类方法之二
    
    
class A:
  def __init__(self):
    self.a = 100
    self.__b = 200
    
  def test1(self):
    print('test1')
    
  def __test2(self):
    print('test2')
    
  def test3(self): # 可以访问私有属性和方法
    print(self.__b)  
    print(self.__test2())
    
class B(A):
  def test4(self): # 不可以访问私有属性和方法
    print(self.__b)
    print(self.__test2())
```

#### 多继承

```python
class Base:
  def test(self):
    print('base')
    
class A(Base):
  def test1(self):
    print('test1')
   
  def test(self):
    print('A')
    
class B(Base):
  def test2(self):
    print('test1') 
    
  def test(self):
    print('B') 
    
class C(A, B):
  pass


print(C.__mro__) # 类的继承顺序，决定了方法被调用的顺序(c3算法)
c = C()
c.test() # 根据__mro__方法调用顺序确定
```

### 类的属性和方法

```python
class Tool(object):
  num = 0 # 类属性
  
  def __init__(self, name):
    self.name = name
    Tool.name += 1  # 注意使用类名调用类属性
    
  @classmethod
  def add_num(cls): # 类方法
    cls.num = 100
    
  @staticmethod
  def print_all():
    print('static')
    

tool = Tool('a') 
Tool.add_num() # 调用类方法
tool.add_num() # 调用类方法
print(Tool.num)
tool.print_all() # 调用静态方法
Tool.print_all() # 调用静态方法
```

### 工厂方法

#### 简单工厂方法

```python
class CarStore(object):
  def __init__(self):
    self.factory = Factory()
  
  def order(self, car_type):
    return self.factory.select_car_by_type(car_type)
    
    
class Car(object):
  def move(self):
    print('moveing')
    
  def stop(self):
    print('stop')
    
class Suonata(Car):
  pass

class Mingtu(Car):
  pass

class Ix35(Car):
  pass

class Factory(object):
  def select_car_by_type(car_type):
    if car_type == 1:
      return Suonata()
    elif car_type == 2:
      return Mingtu()
    elif car_type == 3:
      return Ix35()
```

#### 工厂方法模式

```python
class Store(object):
  def select_car(self, car_type):
    pass
  
  def order(self, car_type):
    return self.select_car(car_type)
  
class BMWCarStore(Store):
  def select_car(self, car_type):
    return BMWFactory.select_car_by_type(car_type)
    
class CarStore(object):
  def __init__(self):
    self.factory = Factory()
  
  def order(self, car_type):
    return self.factory.select_car_by_type(car_type)
    
class Car(object):
  def move(self):
    print('moveing')
    
  def stop(self):
    print('stop')
    
class Suonata(Car):
  pass

class Mingtu(Car):
  pass

class Ix35(Car):
  pass

class BMWFactory(object):
  def select_car_by_type(car_type):
    if car_type == 1:
      return Mini()
    elif car_type == 2:
      return X5()

class Factory(object):
  def select_car_by_type(car_type):
    if car_type == 1:
      return Suonata()
    elif car_type == 2:
      return Mingtu()
    elif car_type == 3:
      return Ix35()
```

### 单例

```python
class Dog(object):
  __instance = None
  
  def __new__(cls):
    if cls.__instance == None:
      cls.__instance = object.__new__(cls)
    
    return cls.__instance
  
a = Dog()
b = Dog()
```

### 实例创建过程

1. 调用`__new__`创建一个实例。
2. 调用`__init__`初始化实例中的属性。

### 嵌套类

```python
class Parent:
    def __init__(self):
        self.name = 'parent'

    def get_name(self):
        print(self.name)

    class Child:
        def __init__(self):
            self.name = 'child'

        def get_name(self):
            print(self.name)

if __name__ == '__main__':
    p = parent()
    p.get_name()
    c = p.child()
    c.get_name()
```

### 私有化

* `xx`：公有变量。
* ` _x`：单前置下划线，私有化属性或方法，from somemodule import *禁止导 入，类对象和子类可以访问。
* ` __xx`：双前置下划线，避免与子类中的属性命名冲突，无法在外部直接访问（名字重整所以访问不到）。
* ` __xx__`：双前后下划线，用户名字空间的魔法对象或属性。例如: `__init__` , 不要自己发明这样的名字。
* `xx_`：单后置下划线，用于避免与Python关键词的冲突。

通过name mangling名字重整（目的就是以防子类意外重写基类的方法或者属性），如：`_Class__object`机制就可以访问private了。

```python
_num # 其他模块不可导入

class Test:
  def __init__(self):
    self.__num = 100 # 私有变量
```

### 属性property

```python
class Money(object):
  def __init__(self):
    self.__money = 0
    
  def getMoney(self):
    return self.__money
  
  def setMoney(self, value):
    if isinstance(value, int):
        self.__money = value 
    else:
      print("error:不是整型数字") 
      
  money = property(getMoney, setMoney)
  
  @property
	def money(self):
		return self.__money
  
  @money.setter
  def money(self, value):
    if isinstance(value, int):
        self.__money = value 
    else:
      print("error:不是整型数字")
```

## 异常处理

```python
try:
  open('a.txt')
  print(num)
except (NameError, FileNotFoundError): # 用同一种方式处理异常
  pass
except FileNotFoundError:
  passs
except Exception as e: # 全部异常
  print(e)
else:  # 没有异常处理
  pass
finally: # 有没有异常都执行
  pass
```

### 抛出异常

```python
class ShortInputError(Exception):
  def __init__(self, msg):
    self.msg = msg

try:
	raise ShortInputError('输入出错')
except ShortInputError as result:  # 将异常对象保存到result中
  print(result.msg)
  raise  # 在异常处理中，重新抛出异常
```

## 模块和包

### 模块

```python
import time as tt # 别名

tt.sleep(3)

import sendmsg # 先搜索当前路径，后搜索系统路径
sendmsg.test1()
sendmsg.test2()

from sendmsg import test1, test2
test1()
test2()

from sendmsg import *
test1()
test2()

__name__ # 模块名称
```

#### 模块导出

```python
__all__ = ['test1', 'test2'] # 可以导出达到功能名称

def test1():
  pass

def test2():
  pass
```

### 包

python每个包中都需要有`__init__.py`文件，该文件可以控制导出模块。

```python
__all__ = ['sendmsg'] # 导出的模块名称

from . import sendmsg # 可以使用[包名.模块名.方法名]调用
```

#### 安装包

在和包并列的路径下创建`setup.py`文件，在文件中写入

```python
from disutils.core import setup

setup(name='hughxuus', version='1.0', description='hughxusu', author='hughxusu', py_modules=['suba.aa', 'suba.bb', 'subb.cc'])
```

文件路径

```shell
.
├── setup.py
├── suba
│   ├── aa.py
│   ├── bb.py
│   └── __init__.py
└── subb
    ├── cc.py
    ├── dd.py
    └── __init__.py
```

安装命令

```shell
python setup.py build
python setup.py sdist

# 对dist包解压
python setup.py install
```

## 生成器与迭代器

### 生成器

在Python中，这种一边循环一边计算 的机制，称为生成器：generator。

#### 列表生成器

```python
G = (x*2 for x in range(5))

next(G) # 获取生成器的值
```

#### 生成器函数

```python
def fib(times):
  n = 0
  a, b = 0, 1
  while n < times:
    yield b
    a, b = b, a + b
    n += 1
  
  return 'done'

F = fib(5)
next(F)
F.__next__() # 获得生成值

for n in fib(5):
  print(n)
  
g = fib(5)
while True:
  try:
    x = next(g)
    print("value:%d" % x)
  except StopIteration as e:
    print("生成器返回值:%s" % e.value)
    break
```

#### `send`

```python
def gen():
  i = 0
  while i < 5:
    temp = yield i # 下一次调用生成器是可以传入的值赋值给temp
    print(temp)
    i += 1
    
f = gen()
# 直接开始调用send会报错
f.send(None) # 第一次调用需要出入空值
f.send('haha') # 向生成器传入‘haha’
```



### 可迭代对象

迭代是访问集合元素的一种方式。迭代器是一个可以记住遍历的位置的对象。迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

可迭代对象（以直接作用于for循环的数据类）

* 集合数据类型，如 list、tuple、dict、set、str等。
* generator ，包括生成器和带yield的生成函数。

```python
from collections import Iterable

# 判断对象是否可以迭代
isinstance([], Iterable)
```

生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。

### 迭代器

可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。使用 isinstance() 判断一个对象是否是为迭代器。

```python
from collections import Iterator

# 迭代器对象
isinstance((x for x in range(10)), Iterator)

# 将数组转换为迭代器
a = iter([1， 2， 3])
isinstance(a, Iterator)
```

可迭代对象与迭代器：

* 凡是可作用于for循环的对象都是Iterable类型；
* 凡是可作用于next()函数的对象都是Iterator类型；
* 集合数据类型如list、 dict、 str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

## 闭包和装饰器

### 闭包

一个函数与其相关的引用环境组合的一个整体(实体)

```python
#定义一个函数
def test(number):

    #在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，那么将这个函数以及用到的一些变量称之为闭包
    def test_in(number_in):
        print("in test_in 函数, number_in is %d"%number_in)
        return number + number_in
    #其实这里返回的就是闭包的结果
    return test_in
```

#### 闭包应用

```python
def test(a):
  def test_in(b):
    print(a + b)
  return test_in

res = test(100) # 配置函数所需环境
res(1) # 执行函数
```

闭包的调用分两个阶段：

1. 第一次调用配置函数所需环境。
2. 第二次调用获得执行结果。
3. `test_in`函数和`a`变量共同构成了闭包。

闭包的特点

1. 闭包似优化了变量，原来需要类对象完成的工作，闭包也可以完成
2. 由于闭包引用了外部函数的局部变量，则外部函数的局部变量没有及时释放，消耗内存

### 装饰器

装饰器利用了闭包的特性，可以实现回调的效果。

#### 装饰器原理和使用

```python
def w1(func): # 参数中必须有函数
  def inner():
    print('权限验证')
    func() # 函数必须回调
  return inner

def f1():
  print('f1')
  
def f2()
	print('f2')
  
in = w1(f1) # 包装了f1
in()

in = w1(f2) # 包装了f2
in()

f1 = w1(f1) # 重新定义了f1并对其进行了包装

# 只要python解释器执行到装饰器，就自动执行，不需要等到调用的时候
@w1 # 使用装饰器等价于重新定义f3 = w1(f3)
def f3():
  print('f3')
```

#### 带有参数的装饰器

```python
def func(call_back):
  def func_in(a, b): # 内部函数参数需要与被装饰函数一致
    call_back(a, b)
  return func_in

@func
def test(a, b)
		return a + b

def func(call_back):
  def func_in(*args, **kwargs): # 不定长参数
    call_back(*args, **kwargs)
  return func_in

@func
def test(a, b, c)
		return a + b + c
```

#### 带有返回值的装饰器

```python
def func(call_back):
  def func_in():
    ret = call_back()
    return ret # 用于返回被装饰函数的返回值
  return func_in

@func
def test():
  return 'haha'
```

#### 通用装饰器

```python
def func(call_back):
  def func_in(*args, **kwargs): # 不定长参数
    ret = call_back(*args, **kwargs)
    return ret # 返回被装饰函数返回值
  return func_in
```

#### 带有参数的装饰器

```python
def timefun_arg(pre="hello"):
    def timefun(func):
        def wrappedfunc():
            print("%s called at %s %s"%(func.__name__, ctime(), pre))
            return func()
        return wrappedfunc
    return timefun

# 首先执行timefun_arg函数
# @timefun对函数进行装饰
@timefun_arg("itcast") 
def foo():
    print("I am foo")

@timefun_arg("python")
def too():
    print("I am too")

foo()
sleep(2)
foo()

too()
sleep(2)
too()
```

#### 类装饰器

装饰器函数其实是这样一个接口约束，它必须接受一个callable对象作为参数，然后返回一个callable对象。在Python中一般callable对象都是函数，但也有例外。只要某个对象重写了 `__call__()` 方法，那么这个对象就是callable的。

```python
class Test():
    def __call__(self):
        print('call me!')

t = Test()
t()  # call me
# 类装饰器demo

class Test(object):
    def __init__(self, func):
        print("---初始化---")
        print("func name is %s"%func.__name__)
        self.__func = func
    def __call__(self):
        print("---装饰器中的功能---")
        self.__func()
#说明：
#1. 当用Test来装作装饰器对test函数进行装饰的时候，首先会创建Test的实例对象
#   并且会把test这个函数名当做参数传递到__init__方法中，即在__init__方法中的func变量指向了test函数体 
#
#2. test函数相当于指向了用Test创建出来的实例对象
#
#3. 当在使用test()进行调用时，就相当于让这个对象()，因此会调用这个对象的__call__方法
#
#4. 为了能够在__call__方法中调用原来test指向的函数体，所以在__init__方法中就需要一个实例属性来保存这个函数体的引用
#    所以才有了self.__func = func这句代码，从而在调用__call__方法中能够调用到test之前的函数体
@Test
def test():
    print("----test---")
test()
```

## 元类

Python中类同样也是一种对象。

元类就是用来创建这些类的，元类就是类的类。

type就是Python的内建元类，也可以创建自己的元类。

### 动态创建类

```python
def choose_class(name):
  if name == 'foo':
    class Foo(object):
      pass
    return Foo
  else:
    class Bar(object):
      pass
    return Bar
  
MyClass = choose_class('foo')
a = MyClass()
```

### 使用type创建类

type可以接受一个类的描述作为参数，然后返回一个类。

```python
# type(类名, 由父类名称组成的元组(针对继承的情况，可以为空)，包含属 性的字典(名称和值))
Test2 = type("Test2", (), {}) 
t = Test2()
```

#### 使用type创建带有属性的类

```python
Foo = type('Foo', (), {'bar': True})

# 等价于下面代码
# class Foo(object):
#   bar = True
```

#### 使用type创建带有方法的类

```python
def echo_bar(self):
  print(self.bar)
  
FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar}) # 继承自Foo，包含方法echo_bar

FooChild.__class__ # 类对象
```

### `__metaclass__`属性

在定义一个类的时候为其添加`__metaclass__`属性，Python会用`__metaclass__`对应的元类来创建类。

```python
class Foo(object, metaclass=something): # 设置元类
  pass
```

#### 自定义元类

```python
def upper_attr(future_class_name, future_class_parents, future_class_attr):
  newAttr = {}
  
  for name, value in future_class_attr.items():
    if not name.startswith("__"):
      newAttr[name.upper()] = value # 将所有属性变为大写
      
	return type(future_class_name, future_class_parents, newAttr)

class Foo(object, metaclass=upper_attr):
  bar = 'bip'
  
f = Foo()
print(f.BAR)
```

## 其他技术特性

### 作用域

* `globals()`打印全局作用域中的变量
* `locals()`打印函数作用域中的局部变量

#### LEGB规则

Python 使用 LEGB 的顺序来查找一个符号对应的对象

```
locals -> enclosing function -> globals -> builtins
```

* locals，当前所在命名空间(如函数、模块)，函数的参数也属于命名空 间内的变量。
* enclosing，外部嵌套函数的命名空间(闭包中常⻅)。
* globals，全局变量，函数定义所在模块的命名空间。

```python
a=1
def fun():
	# 需要通过 global 指令来声明全局变量
	global a
	# 修改全局变量，而不是创建一个新的 local 变量 a=2
  a = 2
```

* builtins，内建模块的命名空间。

```python
dir(__builtin__) # 查看内建模块
```

### 动态语言

python是动态语言，它是一类在运行时可以改变其结构的语言。

动态语言特性：

* 运行的过程中可以改变变量的类型

* 运行的过程中给对象绑定(添加)属性
* 运行的过程中给类绑定(添加)属性
* 运行的过程中给类绑定(添加)方法

```python
import types

class Person(object):
  def __init__(self, name = None, age = None):
    self.name = name
    self.age = age
    
def run(self, speed):
  print("%s在移动, 速度是 %d km/h"%(self.name, speed))
  

p = Person("老王", 24)
p.run = types.MethodType(run, p) # 通过types给类添加方法可以调用self
p.run(180)
```

* 运行的过程中删除属性、方法

### `__slots__`

Python允许在定义class的时候，定义一个特殊的` __slots__`变量，来限制该class实例能添加的属性。

```python
class Person(object):
  __slots__ = ("name", "age")
  
p = Person()
p.score = 100 # 报错，不允许添加属性
```

## 垃圾回收

### 整数对象池

#### 小整数对象池

Python 对小整数的定义是 [-5, 257) 这些整数对象是提前建立好的，不会被 垃圾回收。在一个 Python 的程序中，所有位于这个范围内的整数使用的都 是同一个对象。单个字母也是这样的。

当定义2个相同的字符串时，引用计数为0，触发垃圾回收。

#### 大整数对象池

每一个大整数，均创建一个新的对象。

#### intern机制

单个单词（不包含空格），不可修改，默认开启intern机制，共用对象，靠引用计数去维护何时释放，引用计数为0，则销毁。

### 回收机制

python采用的是引用计数机制为主，标记-清 除和分代收集两种机制为辅的策略。

循环引用可能造成引用计数失效：数据结构双链表就是循环引用。

针对交叉引用，python通过隔代回收机制清理垃圾。

```python
import gc
gc.disable() # 关闭垃圾回收

import sys
a = 'hello world'
sys.getrefcount(a) # 查看引用计数
```

==重写`__del__`方法而没有调用父类方法会导致内存无法释放==

## 文件操作

### 文件的打开和关闭

文件分类：文本文件/二进制文件

文件的 操作流程：1.打开文件 2.读写文件 3.关闭文件

文件操作方式

| 模式 | 说明                                             |
| ---- | ------------------------------------------------ |
| r    | 只读。文件必须存在。                             |
| w    | 只写。文件已存在覆盖，文件未存在新建。           |
| a    | 追加。文件已存在追加，文件未存在新建。           |
| rb   | 二进制只读。文件必须存在。                       |
| wb   | 二进制只写。文件已存在覆盖，文件未存在新建。     |
| ab   | 二进制追加。文件已存在追加，文件未存在新建。     |
| r+   | 读写。文件必须存在。                             |
| w+   | 读写。文件已存在覆盖，文件未存在新建。           |
| a+   | 读写追加。文件已存在追加，文件未存在新建。       |
| rb+  | 二进制读写。文件必须存在。                       |
| wb+  | 二进制读写。文件已存在覆盖，文件未存在新建。     |
| ab+  | 二进制读写追加。文件已存在追加，文件未存在新建。 |

```python
def run():
    f = open('test.py')
    f.close()

if __name__ == '__main__':
    run()
```

### 文件读写

```python
def run():
    f = open('LICENSE', 'r')
    # print(f.read())  # 文件全部读出
    print(f.read(2))  # 两个字符两个字符读取
    print(f.read(2))
    f.close()

    f = open('demo.txt', 'w')
    f.write('aaa')
    f.close()


if __name__ == '__main__':
    run()
```

#### 文件复制

```python
def run(name):
    old_file = open(name, 'r')
    dot = name.rfind('.')
    new_name = name[:dot] + '[附件]' + name[dot:]
    new_file = open(new_name, 'w')
    content = old_file.read()
    new_file.write(content)
    old_file.close()
    new_file.close()


if __name__ == '__main__':
    run('README.md')
```

#### 行读取

```python
def run(name):
    f = open(name, 'r')
    print(f.readline())  # 读一行
    print(f.readlines())  # 读取到一个列表中，每行为一个元素
    f.close()


if __name__ == '__main__':
    run('README.md')
```

#### 大文件读写

```python
def run(name):
    f = open(name, 'r')
    while True:
        content = f.read(1024)  # 每次读1024个字符
        if len(content) == 0:
            break
        print(content)
    f.close()


if __name__ == '__main__':
    run('LICENSE')
```

#### 文件指针移动

```python
def run(name):
    f = open(name, 'r')
    f.seek(100, 0)  # 100 偏移量  0文件开头 1文件当前位置 2表文件末尾
    print(f.read())
    f.tell()  # 获取文件当前位置
    f.close()


if __name__ == '__main__':
    run('LICENSE')
```

### 文件相关操作

```python
import os

def run():
    os.rename('LICENSE', 'new.txt')
    os.remove('LICENSE')
    os.mkdir('test')
    os.rmdir('test')
    os.getcwd()  # 获得当前路径
    os.chdir()  # 修改路径
    os.listdir()  # 获取文件目录

if __name__ == '__main__':
    run()
```

#### 批量重命名

```python
import os

def run(name):
    file_names = os.listdir(name)
    os.chdir(name)
    for name in file_names:
        print(name)
        os.rename(name, '[京东]' + name)

if __name__ == '__main__':
    run('testing')
```

### `with`操作

with 上下文管理器，可以实现一些自动操作

```python
with open('./1.txt', 'wb') as f: # 打开文件f
  f.write('hello flask') # 自动关闭f文件
  
# with自动操作需要实现如下方法，文件对象中即实现了如下方法
class Foo:
    def __enter__(self): # 进入with语句自动调用
        pass

    def __exit__(self, exc_type, exc_val, exc_tb): # 离开with语句后自动调用，可以捕获异常，exc表示异常参数
        pass

with Foo() as foo:
    print('with操作')
    
    
# with语句相当于try finally的结构
try:
  f = open('./1.txt', 'wb')
finally:
  f.close()
```



## 内建属性、函数与库

### 内建属性

#### 常用内建属性

| 常用专有属性       | 说明                   | 触发方式                              |
| ------------------ | ---------------------- | ------------------------------------- |
| `__init__`         | 构造初始化函数         | 创建实例后,赋值时使用，在`__new__`后  |
| `__new__`          | 生成实例所需属性       | 创建实例时                            |
| `__class__`        | 实例所在的类           | `instance.__class__`                  |
| `__str__`          | 实例字符串表示，可读性 | print(类实例)，如没实现，使用repr结果 |
| `__repr__`         | 实例字符串表示，准确性 | 类实例回⻋或者`print(repr(instance))` |
| `__del__`          | 析构                   | del删除实例                           |
| `__dict__`         | 实例自定义属性         | `vars(instance.__dict__)`             |
| `__doc__`          | 类文档，子类不继承     | help(类或实例)                        |
| `__getattribute__` | 属性访问拦截器         | 访问实例属性时                        |
| `__bases__`        | 类的所有父类 构成元素  | `clazz.__bases__`                     |

#### 属性拦截器

可有拦截属性和方法

```python
class Itcast(object):
  def __init__(self, subject1):
    self.subject1 = subject1
    self.subject2 = 'cpp'
    
  def __getattribute__(self, obj): # 调用属性或方法时是触发
    if obj == 'subject1':
      print('log subject1')
      return 'redirect python'
    else:
      return object.__getattribute__(self, obj)
    	# return self.test 导致循环调用
 
	def show(self):
    print('this is Itcast')
    
s = Itcast("python")
print(s.subject1)
print(s.subject2)
s.show()
```

### 内建函数

#### `print`

```python
name = 'hugh'
age = 20
print('姓名: %s, 年龄: %d'%(name, age))
```

#### `input`

```python
user = input('请输入用户名')
```

#### `eval`

```python
a = 'lambda x, y: x + y'
b = eval(a) # 将字符串转换文语句，即lambda表达式
```

#### `map`

map函数会根据提供的函数对指定序列做映射。

* 第一个参数接收一个函数
* 后面的参数接收序列
* 返回值是一个list

参数序列中的每一个元素分别调用function函数，返回包含每次function函数 返回值的list。

```python
map(lambda x: x*x, [1, 2, 3]) # 函数需要一个参数
# 对数组中每个值平方 [1, 4, 9]

map(lambda x, y: x+y, [1, 2, 3], [4, 5, 6])
# 将两个数组的值分别作和 [5, 7, 9]

def f1( x, y ):
  return (x,y)

l1 = [0, 1, 2, 3, 4, 5, 6]
l2 = ['Sun', 'M', 'T', 'W', 'T', 'F', 'S']
l3 = map(f1, l1, l2)
print(list(l3))
```

#### `filter`

filter函数会对指定序列执行过滤操作

* 第一个参数接受一个参数，返回布尔值True或False
* 后面的参数序列可以是str，tuple，list

filter函数会对序列参数sequence中的每个元素调用function函数，最后返回 的结果包含调用结果为True的元素。返回值的类型和参数sequence的类型相同

```python
filter(lambda x: x%2, [1, 2, 3, 4])
# 返回奇数[1, 3]

filter(None, "she")
```

#### `sorted`

```python
sorted(iterable, cmp=None, key=None, reverse=False) # 返回数组
```

### 库

#### 常用标准库

| 标准库          | 说明                  |
| --------------- | --------------------- |
| builtins        | 内建函数默认加载      |
| os              | 操作系统接口          |
| sys             | Python自身的运行环境  |
| functools       | 常用的工具            |
| json            | 编码和解码JSON对象    |
| logging         | 记录日志，调试        |
| multiprocessing | 多进程                |
| threading       | 多线程                |
| copy            | 拷⻉                  |
| time            | 时间                  |
| datetime        | 日期和时间            |
| calendar        | 日历                  |
| hashlib         | 加密算法              |
| random          | 生成随机数            |
| re              | 字符串正则匹配        |
| socket          | 标准的BSD Sockets API |
| shutil          | 文件和目录管理        |
| glob            | 基于文件通配符搜索    |

#### `hashlib`

```python
import hashlib
m = hashlib.md5() # 创建hash对象
m.update('itcast')
print(m.hexdigest()) # 返回十六进制数字字符串
```

#### `sys`

```python
import sys
sys.getrefcount(a) # 获得对象的引用计数，比实际计数多1

sys.path # 模块搜索路径
sys.path.append('/home') # 增加搜索路径
```

#### `imp`

```python
form imp import reload
reload(test) # 重新加载模块
```

#### `functools`

##### `partial`

把一个函数的某些参数设置默认值，返回一个新的函数，调用这个新函数会 更简单。

```python
import functools

def showarg(*args, **kw):
  print(args)
  print(kw)
  
p1 = functools.partial(showarg, 1,2,3)
p1()

# 后面的调用都会传入1，2，3参数
p1(4, 5, 6)
p1(a='python', b='itcast')

p2 = functools.partial(showarg, a=3, b='linux')
p2()

# 后面的调用都会传入a，b参数
p2(1, 2)
p2(a='python', b='itcast')
```

