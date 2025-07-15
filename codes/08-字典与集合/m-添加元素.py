colors = {'red', 'blue', 'yellow', 'purple'}
colors.add('white')
print(colors)

colors.add('red')
print(colors)

colors.add(10)
print(colors)


colors.update(['gray', 'pink'])
print(colors)

colors.update('black')
print(colors)

colors.update(10) # 输入不是序列参数会报错