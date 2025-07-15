groups = [(i, j) for i in range(1, 3) for j in range(3)]
print(groups)

# 生成一个九九乘法表的列表推导式
nums = [i*j for j in range(1, 10) for i in range(1, j+1)]
print(nums)