# Python中常用的标准库

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
| math            | 常用数学函数库        |

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

`partial`把一个函数的某些参数设置默认值，返回一个新的函数，调用这个新函数会 更简单。

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

