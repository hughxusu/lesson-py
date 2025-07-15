colors = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print(colors)
students = ['Bob', 25, 'bob@web.com']
print(students)

# 使用关键字创建列表
schools = list('对酒当歌，人生几何。')
print(schools)

# 创建空列表
one = []
print(one)
two = list()
print(two)

# 列表的布尔测试: 空列表为False，其它为True
print(bool(one))
print(bool(colors))

flag = False
print(flag or colors)
print(one and colors)
