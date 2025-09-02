# Matplotlib

[Matplotlib](https://matplotlib.org/)是建立在Numpy数组基础上的多平台数据可视化程序库，可以绘制2D和3D的图像。安装Matplotlib

```shell
pip install matplotlib
```

## 基本操作

导入模块

```python
import matplotlib as mpl # 使用高级功能时导入完成包
import matplotlib.pyplot as plt # 常用的绘图工具
```

图像绘制流程：

1. 组织要绘制的数据x和y。
1. 创建画布，可省略。

`plt.figure(figsize=(), dpi=) `  figsize: 指定图的长宽；dpi: 图像的清晰度

2. 绘制图像

`plt.plot(x, y) `x轴坐标（数组），y轴坐标（数组）x轴和y轴数据必须一致

3. 显示图像

`plt.show()`

绘制曲线

```python
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()
```

### Matplotlib图像结构

<img src="https://raw.githubusercontent.com/hughxusu/lesson-py/develop/images/libs/anatomy.png" style="zoom:50%;" />

## 绘制单幅图像

1. 一幅图像中绘制多条曲线。

```python
cosy = np.cos(x)
plt.plot(x, y)
plt.plot(x, cosy)
plt.show()
```

2. 修改曲线的样式

```python
plt.plot(x, cosy, color='r', linestyle='--')
```

[可以选择的颜色](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)和[可以选择的线条样式](https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html)

3. 设置坐标范围

```python
plt.xlim(-5, 15)
plt.ylim(0, 1.5)

# 使用axis条件坐标范围
plt.axis([-1, 11, -2, 2])
```

4. 添加标签

```python
plt.xlabel('x axis')
plt.ylabel('y value')
```

解决中文显示问题

```python
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
```

5. 添加图示

```python
plt.plot(x, y, label='sin(x)')
plt.plot(x, cosy, color='r', linestyle='--', label='cos(x)')
plt.legend() # 绘图前要显示调用图示显示
```

[`plt.legend(loc)`中的`loc`可以调整图例的位置](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend)

6. 添加标题

```python
plt.title('sin & cos')
```

7. 添加网格显示

```python
plt.grid(True, linestyle='--', alpha=0.5) # alphab表示网格线透明度
```

8. 图像保存

```python
plt.savefig("test.png") # 保存图片到指定路径
```

> [!warning]
>
> `plt.show()` 会释放figure资源，如果在显示图像之后保存图片将只能保存空图片。

9. 显示图像

```python
plt.show()
```

## 散点图

1. 绘制散点图

```python
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.scatter(x, y) # 绘制散点图的函数
plt.show()
```

2. 绘制不同数据的散点图

```python
cosy = np.cos(x)
plt.scatter(x, cosy, color='r')
```

散点图绘制特征数据

```python
# 简单模拟
x = np.random.normal(0, 1, 100)
y = np.random.normal(0, 1, 100)

plt.scatter(x, y)
plt.show()

# 模拟均匀分布
x = np.random.normal(0, 1, 10000)
y = np.random.normal(0, 1, 10000)

plt.scatter(x, y, alpha=0.1)
plt.show()
```



