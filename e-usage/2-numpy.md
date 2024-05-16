# Numpy

[Numpy](https://numpy.org/)是一个开源的Python科学计算库，用于矩阵运算。

* Numpy支持常见的数组和矩阵操作。
* Numpy支持数值计算任务。

## Numpy的数据结构

查看Numpy的安装版本

```python
import numpy
numpy.__version__
```

Python中的标准可变多元素容器是列表，Python的列表可以保存不同类型的数据。

```python
l = [i for i in range(10)]
l[5] = 100
l[5] = 'learning numpy'
```

> [!warning]
>
> Python数组的灵活性是以牺牲效率为代价的，包括存储效率和计算效率。

Python中自带存储固定类型的数据。

```python
import array
arr = array.array('i', [i for i in range(10)])
arr[5] = 100
arr[5] = 'learning numpy'
```

> [!warning]
>
> 数组中只保存相同类型的数据可以提高存储效率和操作效率。

Numpy中数组的类型为`ndarray`，可以直接根据Python的列表创建。

```python
import numpy as np

arr = np.array([i for i in range(10)])
arr[5] = 100
arr[5] = 'learning numpy'
```

<img src="../_images/libs/array_vs_list.png" style="zoom:85%;" />

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
print(zeros.dtype) # 默认的数量类型是浮点型。
zeros = np.zeros(10, dtype=int) # 创建整形数组。
```

`np.zeros_like`根据已有形状构造数据。

```python
a = [1, 2, 3]
arr = np.zeros_like(a)
arr
```

2. `np.ones`创建全1数组。

```python
# 创建一个3×5的浮点型数组，数组的值都是1。
ones = np.ones(shape=(3, 5), dtype=float)
```

`np.ones_like` 根据已有形状构造数据。

```python
a = [[1, 2, 3], [4, 5, 6]]
arr = np.ones_like(a)
arr
```

3. `np.full`用特定值填充数组。

```python
# 创建一个3×5的浮点型数组，数组的值都是3.14。
w = np.full(shape=(3, 5), fill_value=3.14)
```

Numpy中创建数组的函数一般都包含`shape`和`dtype`两个参数：

* `shape`接受数字和元组类型，用于控制数组的形状。
* `dtype`用于控制数据的类型，不同创建数组函数默认值有差异，不一定都是`float`类型。

> [!warning]
>
> `ndarray`是Numpy的数组类型，习惯称为数组，但其支持多维数据：
>
> * 行向量或列向量在Numpy中称为数组。
> * 矩阵在Numpy中也称数组。

4. `np.arange`用于生成一个一维数组，类似于Python内置的`range`函数。

```python
arr = np.arange(0, 20, 2)
arr = np.arange(0, 1, 0.2) # arange支持浮点步长
arr = np.arange(0, 10) 
arr = np.arange(10)
```

5. `np.linspace`用于生成指定间隔内的等间距数值序列。`np.linspace(start, stop, num, …)`。
   * `start`数列的起始值。
   * `stop`数列的结束值。
   * `num`生成的等间距数值的数量。默认值为50，包含其实值和结束值

```python
arr = np.linspace(0, 20) 
arr = np.linspace(0, 20, 10)
arr = np.linspace(0, 20, 11)
```

6. `np.array(a, dtype)`和`np.asarray(a, dtype)`从现有数组生成

```python
a = [[1, 2, 3], [4, 5, 6]]
a1 = np.array(a) # 深拷贝
a2 = np.asarray(a) # 浅拷贝
```

#### `np.random`生成随机数据

1. `np.random.randint`生成正数随机数。

```python
arr = np.random.randint(0, 10) # 生成一个随机整数，反正在[0, 10)之间
arr = np.random.randint(0, 10, 10) # 生成一维数组
arr = np.random.randint(0, 1, 10) # 测试随机数的范围
arr = np.random.randint(0, 10, size=10) # 显示指明数组大小
arr = np.random.randint(0, 10, size=(3, 5)) # 生成随机矩阵
```

2. `np.random.seed`指定随机种子，是随机数生成的值相同。

```python
np.random.seed(666)
arr = np.random.randint(4, 8, size=(3, 5))
```

3. `np.random.random`生成[0, 1)之间均匀分布的随机数。该函数不能修改随机范围。

```python
arr = np.random.random(10)
arr = np.random.random((3, 5))
```

4. `np.random.normal`生成正太分布的数组。`np.linspace(loc, scale, …)`。
   * `loc`正太分布的均值，默认值为0。
   * `scale`正太分布的方差，默认值为1。

```python
value = np.random.normal()
value = np.random.normal(10, 100)
arr = np.random.normal(0, 1, (3, 5))
arr = np.random.normal(size=(3, 5))
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
| `unicode_` |                        unicode类型                         | 'U'   |

[`dtype`完整的数据类型](https://www.runoob.com/numpy/numpy-dtype.html)

创建数组的时候指定类型

```python
arr = np.array([1, 2, 3, 4, 5, 6], dtype=np.float32)
arr = np.array(['python', 'tensorflow', 'scikit-learn', 'numpy'], dtype = np.string_)
```

查看`ndarray`中的数据类型，数据类型一旦确定不同类型的数据会进行隐式数据转换。

```python
arr = np.arange(10)
arr[5] = 3.14
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

x.reshape(10, -1) # -1会根据数据数量和行数自动计算合适的列数。
x.reshape(2, -1) 
x.reshape(3, -1) 
```

### 数据访问

使用索引访问数据

```python
x = np.arange(15).reshape(3, 5)
y = np.arange(10)

# 访问一维数组
y[0]
y[-1]

# 访问二维数组
x[0][0] # 类似于python数组访问，不推荐
x[2, 2] # 使用元组访问，等价于x[(2, 2)]，推荐
```

数组的切片

1. 对于一维数组数组切片操作和Python的列表相同。

```python
y[0:5]
y[:5]
y[5:]
y[::2]
y[::-1]
```

2. 二维数组的切片操作。

```python
x[:2, :3] # 前两行前三列。
x[:2, ::2] 
x[::-1, ::-1]

# 读取第一行
x[0]
x[0, :]

# 读取第一列
col = x[:, 0]
print(col.ndim)
print(col.shape)
```

> [!attention]
>
> 1. 对列数据进行切片，切片后数组的形状为`(3,)`，切片后的数据都会以行向量存储。
> 2. 数组切片操作保存到新变量中是引用数据。`reshape`也是引用数据。

```python
sub_x = x[:2, :3]
print(sub_x)
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
np.concatenate([x, y])

a = np.array([[1, 2, 3], [4, 5, 6]])
np.concatenate([a, a])  # 垂直方向进行拼接
np.concatenate([a, a], axis=1) # 水平方向进行拼接

np.concatenate([a, y]) # 向量和矩阵不能直接拼接
np.concatenate([a, y.reshape(1, -1)]) # 需要修改y的形状
```











### 测试 Numpy 的速度

```python
import random
import time
import numpy as np
a = []
for i in range(100000000):
    a.append(random.random())

%time sum1=sum(a)

b=np.array(a)
%time sum2=np.sum(b)
```

## 基本操作

### 修改类型

`arr.astype(type)` 修改数据类型，type 数据类型。

### 数组去重

`np.unique()`

```
temp = np.array([[1, 2, 3, 4],[3, 4, 5, 6]])
np.unique(temp)
```

## 数组运算

### 逻辑运算

```python
score = np.random.randint(40, 100, (4, 5))
score

test_score > 60

score[score > 60] = 1
score
```

### 通用判断函数

```python
np.all(score[0:2, :] > 60) # 判断前向量是否都大于 60
np.any(score[0:2, :] > 80) # 判断前向量是否有值大于 80
```

### 三元运算

```python
temp = score[:, :]
np.where(temp > 60, 1, 0) # 变量大于 60 设置为 1， 否则设置为0

temp = score[:, :]
np.where(np.logical_and(temp > 60, temp < 90), 1, 0) # 逻辑与

temp = score[:, :]
np.where(np.logical_or(temp > 90, temp < 60), 1, 0) # 逻辑或
```

### 统计运算

- min(a, axis) 最小值
- max(a, axis) 最大值
- median(a, axis) 中位数
- mean(a, axis, dtype) 均值
- std(a, axis, dtype) 标准差
- var(a, axis, dtype) 方差

axis = 0 代表按照列统计； axis = 1代表按照行统计。

```python
print(np.max(temp, axis=0))
print(np.min(temp, axis=0))
print(np.std(temp, axis=0))
print(np.mean(temp, axis=0))
```

## 数组间运算

### 数组与数的运算

```python
arr = np.array([[1, 2, 3, 2, 1, 4], [5, 6, 1, 2, 3, 1]])
arr + 1
arr / 2
```

### 广播机制

数组在进行矢量化运算时，要求数组的形状是相等的。当形状不相等的数组执行算术运算的时候，就会出现广播机制，该机制会对数组进行扩展，使数组的shape属性值一样，这样，就可以进行矢量化运算了。下面通过一个例子进行说明：

```python
arr1 = np.array([[0],[1],[2],[3]])
arr1.shape

arr2 = np.array([1,2,3])
arr2.shape

arr1+arr2
```

![](https://s1.ax1x.com/2023/05/22/p9oc4tx.png)

## 矩阵运算

```python
a = np.array([[80, 86],
              [82, 80],
              [85, 78],
              [90, 90],
              [86, 82],
              [82, 90],
              [78, 80],
              [92, 94]])
b = np.array([[0.7], [0.3]])

np.matmul(a, b)
np.dot(a,b)
```

二者都是矩阵乘法。 np.matmul中禁止矩阵与标量的乘法。 在矢量乘矢量的内积运算中，np.matmul与np.dot没有区别。

