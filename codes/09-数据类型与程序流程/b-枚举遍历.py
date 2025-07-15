colors = ['red', 'blue', 'yellow', 'green']

for i in enumerate(colors):
    print(i)

for index, color in enumerate(colors, start=2):
    print(f'索引是{index}, 对应的颜色是{color}')

colors = set(colors)  # 变换集合后顺序会发生变化
for i in enumerate(colors):
    print(i)

person = {
    'name': 'Bob',
    'age': 25,
    'job': 'Dev',
    'city': 'New York',
    'email': 'bob@web.com'
}
for i in enumerate(person):
    print(i)