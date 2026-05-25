# 组合字典，注意数组对齐
keys = ['name', 'age', 'job']
values = ['Bob', 25, 'Dev']
persons = {keys[i]: values[i] for i in range(len(keys))}
print(persons)
