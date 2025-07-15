# 生成字典
nums = {i: i**2 for i in range(1, 5)}
print(nums)

# 组合字典，注意数组对齐
keys = ['name', 'age', 'job']
values = ['Bob', 25, 'Dev']
persons = {keys[i]: values[i] for i in range(len(keys))}
print(persons)

# 字典中提取
stocks = {'apple': 268, 'google': 218, 'twitter': 122, 'facebook': 153, 'tesla': 230}
better = {key: value for key, value in stocks.items() if value >= 200}
print(better)