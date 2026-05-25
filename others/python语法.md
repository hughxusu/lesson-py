# 语法基础

## 类

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

## 模块和包

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

## 垃圾回收

### 整数对象池

#### 小整数对象池

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

## 内建属性、函数与库

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







