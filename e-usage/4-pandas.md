# Pandas

[Pandas](https://pandas.pydata.org/)是在Numpy基础上建立的数据处理库，非常适合处理表格数据，例如电子表格或数据库表。

Pandas主要用于数据分析和数据清理等相关任务。

> [!warning]
>
> 在拥有16GB内存的计算机上，pandas可以轻松处理数百万行、数十个列的数据集。
>
> `int64`和`float64`：每个元素占8个字节。
>
> 内存 $ =\text{rows}\times\text{columns}\times\text{bytes}=1,000,000\times10\times8=80\text{MB}$

## Pandas数据结构

Pandas中一共有三种数据结构，分别为：Series、DataFrame和Panel。

* Series是一维数据结构，
* DataFrame是二维数据结构。
* Panel是三维数据结构。

> [!warning]
>
> Panel数据结构很少使用，通常使用其他方式替代这种数据结构。

### DataFrame数据结构

创建一个DataFrame的数据结构

```python
import pandas as pd

# 从网络读取数据
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")  
print(type(stock_df)) # 查看数据结构
```

DataFrame是一个类似于表格的数据结构，可以保存任何类型数据（比如整数、字符串、浮点数等）。

* 有`index`行索引对应的轴为0，`columns`列索对应的轴为1。
* 如果没有传入索引参数，则默认会自动创建一个从0-N的整数索引。

<img src="https://raw.githubusercontent.com/hughxusu/lesson-py/developing/_images/libs/creating_dataframe1.png" style="zoom:65%;" />

DataFrame的基本属性

* Numpy的属性`shape`、`dtypes`、`ndim`
* DataFrame属性：
  * 获得索引`index`、`columns`
  * `values`获得数据矩阵，返回数据类型是Numpy数组。
  * `T`对DataFrame数据进行转置。

```python
print(data.shape)
print(data.index)
print(data.columns)
print(type(data.values))
data.values
data.T
```

DataFrame的整体查询`head()`和`tail`可以查询头部和尾部的数据，默认是5条数据。

```python
data.head()
data.tail(10)
```

#### DataFrame的索引

索引包含`index`和`columns`用于数据查询，可以看作是一个**不可变数组**或有序集合，为任意类型数据。

```python
print(type(players.index))
print(type(players.columns))
```

1. 修改行列索引值。

> [!attention]
>
> DataFrame修改`index`或`columns`的操作，不能修改单个值，只能整体全部修改。

```python
print(data.index[0])
data.index[0] = 'Avery Bradley' # 报错不能修改单个值

index = data.index.tolist() # 将index转换为list
index[0] = 'Avery Bradley'
data.index = index
```

2. `index`的设置与重置。设置与重置的操作只针对`index`，`columns`没有该操作。

`set_index`可以将某一列数据设置为索引。同时可以设置多重索引。

```python
players = data.set_index('Name') # 将球员的名字设置为索引
print(players.index)

players = data.set_index(['Name', 'Team'])
print(players.index)
```

> [!warning]
>
> 设置多个索引的操作将数据变为了基于MutiIndex的DataFrame数据结构。

`reset_index`将原来的索引删除或变为一列数据。

```python
data = players.reset_index() # 将原来索引变为一列数据
temp = players.reset_index(drop=True) # 删除原来索引
```

### Series

Series是一维标记数组，只有行索引没有列索引，够保存任何类型的数据。

从DataFrame中获取一个Series数据

```python
players = data.set_index('Name')
salary = players['Salary']

print(type(salary))
print(salary.index)
print(salary.columns)
```

### 创建数据

#### 创建Series数据

`pd.Series(data, index=index)`

* `data`：传入的数据，参数支持多种数据类型，包括ndarray、list、dict等。
* `index`：可选参数，与数据的长度相等，默认会自动创建一个从0-N的整数索引。

```python
pd.Series([2, 4, 6])
pd.Series(5, index=[100, 200, 300])
pd.Series(np.arange(10))
population_dict = {
    'California': 38332521,
    'Texas': 26448193,
    'New York': 19651127,
    'Florida': 19552860,
    'Illinois': 12882135
}
population = pd.Series(population_dict)
```

#### 创建DataFrame数据

`pd.DataFrame(data, index=index, columns=index)`，`data`支持多种数据类型，`indes`和`columns`为可选参数。

```python
# 通过单个Series对象创建
pd.DataFrame(population, columns=['population'])

# 通过字典列表创建
data = [{'a': i, 'b': 2 * i} for i in range(3)]
pd.DataFrame(data)

# 通过Series对象字典创建。
area_dict = {
    'California': 423967, 
    'Texas': 695662, 
    'New York': 141297,
    'Florida': 170312, 
    'Illinois': 149995
}
area = pd.Series(area_dict)
pd.DataFrame({'population': population, 'area': area})

# 通过NumPy二维数组创建。
pd.DataFrame(np.random.rand(3, 2), columns=['foo', 'bar'], index=['a', 'b', 'c'])
```

## 数据取值与修改

### 读取数据

DataFramed数据有三种获取方式

1. 直接使用行列索引<span style="color: #ff4d4f;">（注意：索引方式为先列后行，与Numpy相反）</span>，直接索引支持切片操作。

```python
import pandas as pd

data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")  
players = data.set_index('Name')

players['Salary'] # 获取一列数据，返回Series数据类型
players[['Salary', 'Team', 'Number']] # 获取多列数据，返回DataFramed数据类型
players['Salary']['Avery Bradley']

players['Avery Bradley'] # 直接获取一行数据报错

players['Salary'][0:6]
players[0:3][0:6]
```

> [!attention]
>
> 直接索引不支持Numpy类似的操作

```python
# 下列操作报错
players[2, 2]
players[0:2, 1:3]
```

2. 结合`loc`和`iloc`使用索引，可以先行后列进行索引，支持切片操作。

* `loc`通过名字取值。

```python
players.loc['Avery Bradley', 'Salary']
players.loc['Avery Bradley': 'R.J. Hunter']
players.loc['Avery Bradley': 'R.J. Hunter', ['Salary', 'Team', 'Number']]
```

* `iloc`通过下标进行取值（与Numpy用法相似）。

```python
players.iloc[0, 0]
players.iloc[0: 10, 0:2]
```

3. 混合索引，`loc`、`iloc`和直接索引。

```python
# 使用loc和iloc混合索引数据
players.iloc[0: 10].loc[:, ['Salary', 'Team', 'Number']]

# iloc和直接索引
players.iloc[0: 10]['Salary']
players.iloc[0: 10][['Salary', 'Team', 'Number']]

# 注意：只获取前两行数据不会获取前十行前两列数据
players.iloc[0: 10][0:2]
```

> [!attention]
>
> 老版本中存在`ix`索引，在新版本中已经弃用。

Series数据读取与DataFramed类似也支持`loc`和`iloc`

> [!warning]
>
> 可以把Series对象看成一种特殊的Python字典。

```python
salary = players['Salary']
salary['Avery Bradley']

salary.iloc[10]
salary.iloc[0:5]
```

### 修改数据

修改单个数据应该使用`loc`和`iloc`方法，使用直接索引会产生警告。

```python
players.loc['Avery Bradley', 'Salary'] = 1000
```

修改一列数据可以使用索引

```python
players['Salary'] = 100
players.Salary = 1000
```

### 数据排序

排序有两种形式，一种对于索引进行排序，一种对于内容进行排序，默认值都是从小到大。

1. 使用`sort_values`，可以对单个键或多个键进行排序。

```python
players.sort_values(by='Age')
players.sort_values(by='Age', ascending=False)

# 对多个字段排序传入列表
players.sort_values(by=['Age', 'Weight'], ascending=False) # 降序
```

2. 使用`sort_index`给索引排序。

```python
players.sort_index()
players.sort_index(ascending=False) 
```

## 基本数据操作

### 索引操作

赋值操作

```python
data['close'] = 1
data.close = 1
```

排序

```python
data.sort_values(by="open", ascending=True).head() # 指定排序方式
data.sort_values(by=['open', 'high']) # 按照多个键进行排序
data.sort_index() # 给索引进行排序
```

Series排序

```python
data['p_change'].sort_values(ascending=True).head() # 只有一列
data['p_change'].sort_index().head() # 对索引排序
```

## DataFrame运算

算数运算

```python
# 加减法
data['open'].add(1)
data['open'].sub(1) 
```

逻辑运算

```python
data['open'] > 23

# 使用逻辑运算筛选数据
data[data["open"] > 23].head()
data[(data["open"] > 23) & (data["open"] < 24)].head()
```

逻辑运算函数

```python
data.query("open<24 & open>23").head() # 查询结构
data[data["open"].isin([23.53, 23.85])] # 判断数据是否存在
```

## 统计运算

综合分析: 能够直接得出很多统计结果`count`, `mean`, `std`, `min`, `max` 等

```python
data.describe()
```

对于单个函数去进行统计的时候，坐标轴还是按照默认列“columns” (axis=0, default)，如果要对行“index” 需要指定(axis=1)

```python
data.max(0) # 最大值
data.var(0) # 方差
data.std(0) # 标准差
data.median(0) # 中位数

data.idxmax(0) # 求出最大值的位置
data.idxmin(0) # 求出最小值的位置
```

自定义运算

```python
data[['open', 'close']].apply(lambda x: x.max() - x.min(), axis=0)
```

## 文件读取

Pandas 支持多种文档的存储和读取

<img src="https://pic2.zhimg.com/80/v2-da9199587b07a792a5af6e09aafd6899_1440w.webp" style="zoom:67%;" />

### CSV 文件

```python
data = pd.read_csv("./data/stock_day.csv", usecols=['open', 'close']) # 读取指定列数据
data[:10].to_csv("./data/test.csv", columns=['open']) # 保存数据到csv文件
data[:10].to_csv("./data/test.csv", columns=['open'], index=False) # 保存数据删除索引
```

### HDF5文件

HDF5文件的读取和存储需要指定一个键，值为要存储的DataFrame

```python
data.to_hdf('./test.h5', key='data') # 保存 HDF5格式 key存储标识符
data.read_hdf('./test.h5', key='data') # 读取文件
```

### JSON

JSON是一种前后端的交互经常用到数据格式，是一种键值对形式。

```python
json_read.to_json("./data/test.json", orient='records', lines=True) # 保存文件 orient josn 的存储形式 line 是否为一个对象一行
json_data = pd.read_json('./test.json') # 读取json文件
```

## 缺失值处理

```python
movie = pd.read_csv("./data/IMDB-Movie-Data.csv")

pd.notnull(movie) # 判断是否存在确实值
pd.isnull(movie) 
```

缺失值处理

```python
data = movie.dropna() # 移除缺失值
movie['Revenue (Millions)'].fillna(movie['Revenue (Millions)'].mean(), inplace=True) # 用平均值替换缺失值

data.replace(to_replace='?', value=np.nan) # 替换部分值
```

## 数据离散化

连续属性离散化的目的是为了简化数据结构，数据离散化技术可以用来减少给定连续属性值的个数。离散化方法经常作为数据挖掘的工具。

```python
qcut = pd.qcut(p_change, 10) # 自行分组
qcut.value_counts() # 计算到每个分组中的数据数目

bins = [-100, -7, -5, -3, 0, 3, 5, 7, 100]
p_counts = pd.cut(p_change, bins) # 自己指定分组区间

dummies = pd.get_dummies(p_counts, prefix="rise") # 生成 one-hot 编码
```

## 数据合并

将多张表中的数据合并后一起分析

```python
pd.concat([data, dummies], axis=1) # 按行索引
```

数据合并

```python
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                        'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                        'key2': ['K0', 'K0', 'K0', 'K0'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})

result = pd.merge(left, right, on=['key1', 'key2']) # 内链接
result = pd.merge(left, right, how='left', on=['key1', 'key2']) # 左链接
result = pd.merge(left, right, how='right', on=['key1', 'key2']) # 右链接
result = pd.merge(left, right, how='outer', on=['key1', 'key2']) # 外链接
```

## 案例

数据来源：https://www.kaggle.com/damianpanek/sunday-eda/data

> [!tip]
>
> 1. 我们想知道这些电影数据中评分的平均分，导演的人数等信息，我们应该怎么获取？
> 2. 对于这一组电影数据，如果我们想rating，runtime的分布情况，应该如何呈现数据？
> 3. 对于这一组电影数据，如果我们希望统计电影分类(genre)的情况，应该如何处理数据？

读取数据

```python
import pandas  as pd
import numpy as np
from matplotlib import pyplot as plt

path = "./IMDB-Movie-Data.csv"
df = pd.read_csv(path)
```

案例 1

```python
df["Rating"].mean() # 得出评分的平均分
np.unique(df["Director"]).shape[0] # 得出导演人数信息
```

案例 2

```python
# 绘制得分直方图
plt.figure(figsize=(20,8),dpi=80)

max_ = df["Rating"].max()
min_ = df["Rating"].min()

t1 = np.linspace(min_,max_,num=21)
plt.xticks(t1)

plt.grid()
plt.hist(df["Rating"].values,bins=20)

plt.show()

# 绘制时间分布图
plt.figure(figsize=(20,8),dpi=80)
plt.hist(df["Runtime (Minutes)"].values,bins=20)

max_ = df["Runtime (Minutes)"].max()
min_ = df["Runtime (Minutes)"].min()

t1 = np.linspace(min_,max_,num=21)
plt.xticks(t1)
plt.grid()

plt.show()
```

案例 3

```python
temp_list = [i.split(",") for i in df["Genre"]]
genre_list = np.unique([i for j in temp_list for i in j])

for i in range(1000):
    temp_df.loc[i, temp_list[i]]=1
    
temp_df.sum().sort_values(ascending=False).plot(kind="bar",figsize=(20,8),fontsize=20,colormap="cool")
```

