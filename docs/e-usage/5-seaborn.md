# Seaborn

[Seaborn](https://seaborn.pydata.org/)是一个基于Matplotlib的Python数据可视化库，它提供了一个高级接口，用于绘制有吸引力且信息丰富的统计图形。同时Seaborn可以与Pandas 无缝集成，支持DataFrame数据结构。Seaborn的设计理念

* 数据集导向的API设计。Seaborn是绕数据集（Dataset）而非图形元素进行设计。
* 语义映射系统。将数据维度映射到视觉属性的系统。
* 统计聚合与可视化集成。可视化不是画点，而是展示统计关系。

| **维度** | **Matplotlib**       | **Seaborn**      |
| :------- | :------------------- | :--------------- |
| 设计目标 | 精确控制每个图形元素 | 快速生成统计图形 |
| API思维  | 如何画图形           | 如何展示数据关系 |
| 数据接口 | 数组/列表            | Pandas DataFrame |
| 默认输出 | 基础但可定制         | 统计优化+美观    |
| 学习曲线 | 陡峭（需理解底层）   | 平缓（专注数据） |

安装Seaborn

```shell
pip install seaborn
```

导入Seaborn

```python
import seaborn as sns
```

## 数据可视化

> [!think]
>
> 

* 对于单变量的数据，可以采⽤直⽅图或核密度曲线来展示数据。
* 对于双变量来说，散点图、⼆维直⽅图、核密度估计图形等。



> [!tip]



> [!note]

> [!warning]



> [!alert]
