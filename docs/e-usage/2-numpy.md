# Numpy

[Numpy](https://numpy.org/)是一个开源的Python科学计算库，用于矩阵运算。

* Numpy支持常见的数组和矩阵操作。
* Numpy支持数值计算任务。

安装Numpy

```shell
pip install numpy
```

## Numpy的数据结构

查看Numpy的安装版本

```python
import numpy
numpy.__version__
```

Python中的标准可变多元素容器是列表，Python的列表可以保存不同类型的数据。

```python
l = [i for i in range(10)]
print(l)

l[5] = 100
print(l)

l[5] = 'learning numpy'
print(l)
```

> [!warning]
>
> Python数组的灵活性是以牺牲效率为代价的，包括存储效率和计算效率。

Python中自带存储固定类型的数据。

```python
import array
arr = array.array('i', [i for i in range(10)])
print(arr)

arr[5] = 100
print(arr)

arr[5] = 'learning numpy'
```

> [!warning]
>
> 数组中只保存相同类型的数据可以提高存储效率和操作效率。

Numpy中数组的类型为`ndarray`，可以直接根据Python的列表创建。

```python
import numpy as np

arr = np.array([i for i in range(10)])
print(arr)
print(type(arr))

arr[5] = 100
print(arr)

arr[5] = 'learning numpy'
```

<img src="https://raw.githubusercontent.com/hughxusu/lesson-py/develop/images/libs/array_vs_list.png" style="zoom:85%;" />

* Numpy专门针对`ndarray`的操作和运算进行了设计，所以数组存取和计算性能远优于Python列表，数组越大Numpy的优势就越明显。
* Numpy内置了并行运算功能，会自动做并行计算。
* Numpy底层使用C语言编写，内部解除了GIL（全局解释器锁）。

可以通过`dtype`属性查看数组的类型。

```python
print(arr.dtype)
```

### `ndarray`的创建

除了根据列表来创建数组外，Numpy内置一些函数可以辅助数组的创建。

1. `np.zeros`创建全0数组。

```python
# 创建一个长度为10的数组，数组的值都是0。
zeros = np.zeros(10)
print(zeros)
print(zeros.dtype) # 默认的数量类型是浮点型。

zeros_two = np.zeros(10, dtype=int) # 创建整形数组。
print(zeros_two)
print(zeros_two.dtype)
```

`np.zeros_like`根据已有形状构造数据。

```python
a = [1, 2, 3]
arr = np.zeros_like(a)
print(arr)
```

2. `np.ones`创建全1数组。

```python
# 创建一个3×5的浮点型数组，数组的值都是1。
ones = np.ones(shape=(3, 5), dtype=float)
print(ones)
```

`np.ones_like` 根据已有形状构造数据。

```python
a = [[1, 2, 3], [4, 5, 6]]
arr = np.ones_like(a)
print(arr)
```

3. `np.full`用特定值填充数组。

```python
# 创建一个3×5的浮点型数组，数组的值都是3.14。
w = np.full(shape=(3, 5), fill_value=3.14)
print(w)
```

Numpy中创建数组的函数一般都包含`shape`和`dtype`两个参数：

* `shape`接受数字和元组类型，用于控制数组的形状。
* `dtype`用于控制数据的类型，不同创建数组函数默认值有差异，不一定都是`float`类型。

> [!warning]
>
> `ndarray`是Numpy的数组类型，习惯统称为数组，但其支持多个维度：
>
> * 行向量或列向量在Numpy中，可以用一维数组表示。
> * 矩阵在Numpy中，可以用二维数组表示。

4. `np.arange`用于生成一个一维数组，类似于Python内置的`range`函数。

```python
arr = np.arange(0, 20, 2)
print(arr)

arr = np.arange(0, 1, 0.2) # arange支持浮点步长
print(arr)

arr = np.arange(0, 10) 
print(arr)
print(arr.dtype)

arr = np.arange(10)
print(arr)
```

5. `np.linspace`用于生成指定间隔内的等间距数值序列。`np.linspace(start, stop, num, …)`。
   * `start`数列的起始值。
   * `stop`数列的结束值。
   * `num`生成的等间距数值的数量。默认值为50，包含其实值和结束值

```python
arr = np.linspace(0, 20) 
print(arr)

arr = np.linspace(0, 20, 10)
print(arr)

arr = np.linspace(0, 20, 11)
print(arr)
```

6. `np.array(a, dtype)`和`np.asarray(a, dtype)`从现有数组生成

```python
a = [[1, 2, 3], [4, 5, 6]]
a1 = np.array(a) # 深拷贝
print(a1)

a2 = np.asarray(a1) # 浅拷贝
print(a2)

a1[0][0] = 100
print(a)
print(a1)
print(a2)
```

#### `np.random`生成随机数据

1. `np.random.randint`生成正数随机数（均匀分布）。

```python
arr = np.random.randint(0, 10) # 生成一个随机整数，反正在[0, 10)之间
print(arr)

arr = np.random.randint(0, 10, 10) # 生成一维数组
print(arr)

arr = np.random.randint(0, 1, 10) # 测试随机数的范围
print(arr)

arr = np.random.randint(0, 10, size=10) # 显示指明数组大小
print(arr)

arr = np.random.randint(0, 10, size=(3, 5)) # 生成随机矩阵
print(arr)
```

2. `np.random.seed`指定随机种子，是随机数生成的值相同。

```python
np.random.seed(666)
arr = np.random.randint(4, 8, size=(3, 5))
print(arr)
```

3. `np.random.random`生成[0, 1)之间均匀分布的随机数。该函数不能修改随机范围。

```python
arr = np.random.random(10)
print(arr)

arr = np.random.random((3, 5))
print(arr)
```

4. `np.random.normal`生成正太分布的数组。`np.linspace(loc, scale, …)`。
   * `loc`正太分布的均值，默认值为0。
   * `scale`正太分布的方差，默认值为1。

```python
value = np.random.normal()
print(value)

value = np.random.normal(10, 100)
print(value)

arr = np.random.normal(0, 1, (3, 5))
print(arr)

arr = np.random.normal(size=(3, 5))
print(arr)
```

### `ndarray`的类型

Numpy数组包含同一类型的值，使用`dtype`属性可以查看数据类型，Numpy支持的常用数据类型如下表。

|  数据类型  |                            描述                            | 简写  |
| :--------: | :--------------------------------------------------------: | ----- |
|  `bool_`   |       布尔值（真、True 或假、False），用一个字节存储       | 'b'   |
|   `int_`   | 默认整型（类似于C语言中的long，通常情况下是int64或int32）  | 'i8'  |
|  `int64`   | 整型（范围从 –9223372036854775808 到 9223372036854775807） | 'i8'  |
|  `uint8`   |               无符号整型（范围从 0 到 255）                | 'u'   |
|  `uint16`  |              无符号整型（范围从 0 到 65535）               | 'u2'  |
|  `float_`  |                     float64 的简化形式                     | 'f8'  |
| `float64`  |   双精度浮点型：符号比特位，11 比特位指数，52 比特位尾数   | 'f8'  |
| `complex_` |                复数，由两个 64 位浮点数表示                | 'c16' |
| `object_`  |                         python对象                         | 'O'   |
| `string_`  |                           字符串                           | 'S'   |

[`dtype`完整的数据类型](https://www.runoob.com/numpy/numpy-dtype.html)

> [!warning]
>
> 如果Numpy中保存了`object_`数据类型，本质上和Python的`list`数据没有区别，保存的是对象的地址。

创建数组的时候指定类型

```python
arr = np.array([1, 2, 3, 4, 5, 6], dtype=np.float32)
print(arr)
```

查看`ndarray`中的数据类型，数据类型一旦确定不同类型的数据会进行隐式数据转换。

```python
arr = np.arange(10)
print(arr)
print(arr.dtype)

# 强制转换为整形
arr[5] = 3.14
print(arr)
print(arr.dtype)

# 创建浮点数据类型。
arr2 = np.array([1, 2, 3.14])
print(arr2.dtype)
```

### Numpy的基本属性

数组属性反映了数组本身固有的信息，常用的属性如下表：

| 属性名字 |     属性解释     |
| :------: | :--------------: |
| `shape`  |  数组维度的元组  |
|  `ndim`  |     数组维数     |
|  `size`  | 数组中的元素数量 |
| `dtype`  |  数组元素的类型  |

```python
x = np.arange(15).reshape(3, 5)
y = np.arange(10)
print(x)
print(y)

# 数组的维度
print(x.ndim)
print(y.ndim)

# 数组的形状
print(x.shape)
print(y.shape)

# 数组中的元素数量
print(x.size)
print(y.size)
```

> [!warning]
>
> Numpy中的数据在内存中都是一维连续存储的，`shape`属性只是标注数据的形状。

## 数据操作

### 修改形状

使用`reshape`函数可以修改数组的形状。

```python
x = np.arange(10)
print(x.ndim)

w = x.reshape(2, 5)
print(w.ndim)

w = x.reshape(10, -1) # -1会根据数据数量和行数自动计算合适的列数。
print(w)

w = x.reshape(2, -1) 
print(w)

w = x.reshape(3, -1) 
print(x)
```

### 数据访问

使用索引访问数据

```python
x = np.arange(15).reshape(3, 5)
y = np.arange(10)
print(x)
print(y)

# 访问一维数组
print(y[0])
print(y[-1])

# 访问二维数组
print(x[2, 2]) # 使用元组访问，等价于x[(2, 2)]，推荐
```

数组的切片

1. 对于一维数组数组切片操作和Python的列表相同。

```python
print(y[0:5])
print(y[:5])
print(y[5:])
print(y[::2])
print(y[::-1])
```

2. 二维数组的切片操作。

```python
print(x[:2, :3]) # 前两行前三列。
print(x[:2, ::2])

# 反转数组
print(x[::-1, ::-1])  

# 读取第一行
print(x[0])
print(x[0, :])

# 读取第一列
col = x[:, 0]
print(col.ndim)
print(col.shape)
```

> [!attention]
>
> 1. 对列数据进行切片，切片后数组的形状为`(length,)`，切片后的数据都会以行向量存储。
> 2. 数组切片操作保存到新变量中是引用数据。`reshape`也是引用数据。

```python
sub_x = x[:2, :3]
print(sub_x)
print(x)

sub_x[0, 0] = 100
print(sub_x)
print(x)

x[0, 0] = 0
print(x)
print(sub_x)
```

数据拷贝

```python
sub_x = x[:2, :3].copy()
sub_x[0, 0] = 100
print(sub_x)
print(x)
```

### 数组合并

`concatenate`可以用于数组间的链接

```python
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
print(x)
print(y)
print(np.concatenate([x, y]))

a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.concatenate([a, a]))  # 垂直方向进行拼接
print(np.concatenate([a, a], axis=1)) # 水平方向进行拼接

np.concatenate([a, y]) # 向量和矩阵不能直接拼接
w = np.concatenate([a, y.reshape(1, -1)]) # 需要修改y的形状
print(w)
```

> [!attention]
>
> `concatenate`合并后的数组不是引用数据，是将数据拷贝后生成新的数组，修改原数组或新数组中的数据彼此间不受影响。
>
> 判断操作是不是引用操作主要看操作结果是否是原数组的子集，如果是子集一般为引用操作，如果不是子集一般为拷贝操作。

```python
w[0, 0] = 100
print(w)
print(x)
```

`vstack`将数组在垂直方向拼接，`hstack`将数组在水平方向进行合并。这两个方法支持，矩阵和向量间的操作，但要求数据对齐。

```python
print(np.vstack([a, y]))

b = np.full((2, 2), 100)
print(b)
print(np.hstack([a, b]))

print(np.hstack([a, y])) # 报错，数据在水平方向没有对齐。
```

### 数据分割

`split`函数可以对数组进行分割。

```python
x = np.arange(10)
x1, x2, x3 = np.split(x, [3, 7]) # 第二个参数为分割点，参数形式必须是数组。
print(x1, x2, x3)
w1, w2 = np.split(x, [5])
print(w1, w2)

x1[0] = 100
print(x1)
print(x)

a = np.arange(16).reshape(4, 4)
a1, a2 = np.split(a, [2])  # 在水平方向上分割矩阵
print(a)
print(a1)
print(a2)

a1, a2, a3 = np.split(a, [2, 3], axis=1) # 在垂直方向上进行分割
print(a)
print(a1)
print(a2)
print(a3)
```

`vsplit`在垂直方向进行分割，`hsplit`在水平方向上进行分割。

```python
upper, lower = np.vsplit(a, [2])
print(upper)
print(lower)

left, right = np.hsplit(a, [2])
print(left)
print(right)

# 获取最后一列，并转换为一维数组
x, y = np.hsplit(a, [-1])
y = y[:, 0] 
print(y)
```

## 矩阵运算

### 通用函数

> [!tip]
>
> 给定一个向量长度为一百万，让向量中每个数都乘以2。

Python语言自身的处理方法

```python
n = 1000000
l = [i for i in range(n)]

# 使用for循环处理，并计时
%%time
double = []
for i in l:
    double.append(2 * i)
print(f"列表长度: {len(double)}")
print("前10个元素:", double[:10])  
    
# 使用列表生成式
%%time
double = [2 * i for i in l]
print(f"列表长度: {len(double)}")
print("前10个元素:", double[:10]) 
```

使用Numpy的处理方法

```python
l = np.arange(n)

%%time
double = np.array(2 * i for i in l)

%%time
double = 2 * l # Numpy支持向量与常数的运算操作
print(double)
```

Numpy中将数组作为向量和矩阵进行运算称为通用函数（Universal Function），通用函数的主要目的是对NumPy数组中的值执行更快的重复操作。

通用函数常见的运算符操作

```python
x = np.arange(1, 16).reshape(3, 5)

print(x + 1)
print(x - 1)
print(x * 2)
print(x / 2)
print(x // 2)
print(x ** 2)
print(x % 2)
print(1 / x)
```

> [!warning]
>
> 这里虽然使用的数学符号，但是调用的是Numpy的函数，Numpy重写了这些符号的操作函数，方便程序员使用。
>
> [符号操作重写的方法](附录.md)

通用函数常见的数学函数

```python
print(np.abs(x))
print(np.sin(x))
print(np.cos(x))
print(np.tan(x))
print(np.exp(x))
print(np.power(3, x)) # 等价于x ** 3
print(np.log(x)) # 已e为底的对数
print(np.log2(x))
print(np.log10(x))
```

### 矩阵运算

Numpy中矩阵间运算符的操作，相当于矩阵对应位置元素的运算。

```python
a = np.arange(4).reshape(2, 2)
b = np.full((2, 2), 10)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

数学定义的矩阵运算

```python
print(a.dot(b)) # 矩阵乘法
print(a.T) # 矩阵的转置
```

矩阵求逆。计算函数在`np.linalg`为Numpy线性代数工具包。

```python
inv_a = np.linalg.inv(a)

print(a.dot(inv_a)) # 原局长和逆矩阵矩阵乘法得到单位阵
print(inv_a.dot(a))
```

> [!attention]
>
> 1. 矩阵间的符号运算，要求两个矩阵的形状相同或满足广播机制。
> 2. 矩阵间的数学运算，要求矩阵满足数学运算的条件。

伪逆矩阵

除此之外矩阵的数学运算还包括：伪逆矩阵、求内积、求范数等，可以查阅Numpy手册。

### 向量和矩阵间的运算

Numpy中向量和矩阵的运算，相当于向量和矩阵的每一行对应位置的元素进行运算

```python
v = np.array([1, 2])
print(v + a)
print(v * a)
```

`tile`向量的堆叠

```python
print(np.tile(v, (2, 1))) # 水平方向上堆叠2次，垂直方向闪堆叠1次。
print(np.tile(v, (2, 2)))

print(np.tile(v, (2, 1)) + a) # 与v+a操作相同
```

向量和矩阵的数学运算

```python
print(v.dot(a))
print(a.dot(v)) # Numpy可以自动转换向量形式与矩阵进行运算
```

> [!warning]
>
> 向量和矩阵运算时，无论是行向量还是列向量都表示成一维向量，Numpy会自动进行行向量和列向量的转换。
>
> Numpy中矩阵间运算和矩阵与向量的运算需要注意两个条件：
>
> 1. 两个数组的形状是否满足对齐运算条件。
> 2. 两个数组的形状是否满足数学运算条件。

### 聚合运算

Numpy中的聚合函数用于计算数组的统计值等，Numpy中的聚合函数可以直接作用于数组。

```python
big_array = np.random.random(1000000)
%time sum(big_array)
%time np.sum(big_array)
```

Numpy聚合操作方式

```python
print(np.min(big_array))
np.max(big_array)

# 部分聚合操作可以通过向量直接调用
print(big_array.min())
print(big_array.max())
print(big_array.sum())

# 聚合运算默认是对整个数组进行计算
x = np.arange(16).reshape(4, 4)
print(np.sum(x))

# 指定方向的求和
print(np.sum(x, axis=0)) # 在水平方向进行压缩
print(np.sum(x, axis=1)) # 在垂直方向进行压缩，计算结果仍未一维向量。
```

Numpy中常用聚合操作

```python
print(np.prod(x+1)) # 将所有数相乘
print(np.mean(x)) # 求均值
print(np.median(x)) # 求中位数
print(np.var(big_array)) # 求方差
print(np.std(big_array)) # 求标准差
```

#### `arg`函数

用于获得聚合值的索引

```python
x = np.random.normal(0, 1, size=1000000)
print(np.argmin(x)) # 获得最小值位置索引
print(np.argmax(x)) # 获得最大值位置索引
```

### 数组排序

数组排序

```python
x = np.arange(16)
np.random.shuffle(x) # 将数组打乱
print(x)

z = np.sort(x) # 排序后返回新数组，x顺序不变
print(z)

x.sort() # 对x自身排序
print(x)
```

矩阵排序

```python
x = np.random.randint(10, size=(4, 4))

print(np.sort(x)) # 对每一行数据进行排序
print(np.sort(x, axis=0)) # 沿着水平方向进行排序
```

排序中的索引

```python
x = np.arange(16)
np.random.shuffle(x)
print(x)

print(np.argsort(x)) # 返回排序后数字的索引值，对矩阵同样成立
```

### Fancy Indexing

传递一个索引数组来一次性获得多个数组元素。

向量的索引

```python
x = np.arange(16)
print(x)

# 指定特定元素的索引
index = [3, 5, 8]
print(x[index])

# 根据原数组索引生成二维矩阵
index = np.array([[0, 2], [1, 3]])
print(x[index])
```

矩阵的索引

```python
w = x.reshape(4, -1)

row = np.array([0, 1, 2])
col = np.array([1, 2, 3])
print(w[row, col])
print(w[0, col])
print(w[:2, col])
```

布尔索引

```python
col = [True, False, True, True]
print(w[1:3, col])
```

### 布尔运算

与通用运算类似，得到一个全部是布尔值的数组。支持的运算主要是比较运算。

```python
x = np.arange(16)
print(x)

print(x < 3)
print(x > 3)
print(x <= 3)
print(x >= 3)
print(x == 3)
print(x != 3)

w = x.reshape(4, -1)
print(w < 6)
```

布尔运算的应用

```python
print(np.sum(x <= 3))  # 统计小于3数据的数量
print(np.count_nonzero(x <= 3))  # 统计0元素
```

1.  `any`判断数组是否有True值。

```python
print(np.any(x == 0)) # 是否存等于0的元素
print(np.any(x < 0)) # 是否存在小于0的元素
```

2. `all`判断数组中所有的元素都为True.

```python
print(np.all(x >= 0)) # 全部元素都大于等于0
print(np.all(x > 0)) # 全部元素大于0
```

矩阵运算中的应用

```python
print(np.sum(w % 2 == 0)) # 判断矩阵中有多少偶数
print(np.sum(w % 2 == 0, axis=1)) # 计算每一列有多少偶数
print(np.all(w > 0, axis=1)) # 判断在列方向上是否全部大于0
```

与或非运算

```python
print(np.sum((w > 3) & (w < 10))) # 与运算
print(np.sum((w % 2 == 0) | (w > 10))) # 或运算
print(np.sum(~(w == 0))) # 非运算
```

布尔索引的应用

```python
print(x[x < 5]) # 索引小于5的值
print(x[x % 2 == 0]) # 所有的偶数值
print(w[w[:, 3] % 3 == 0, :]) # w最后一列可以被3整除的行构成的数组。
```









