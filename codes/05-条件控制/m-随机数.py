import random  # 首先需要导入随机数的模块工具包

c = random.randint(1, 3)  # 生成的随机数 12 <= n <= 20
print(c)

print(random.randint(20, 20))  # 结果永远是 20
print(random.randint(20, 10))  # 该语句是错误的，下限必须小于上限