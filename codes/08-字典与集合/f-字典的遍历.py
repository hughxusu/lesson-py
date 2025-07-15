person = {
  'name': 'Bob',
  'age': 25,
  'job': 'Dev',
  'city': 'New York',
  'email': 'bob@web.com'
}

for value in person:
    print(value)


print(person.keys()) # 可迭代对象类似于数组
for key in person.keys():
    print(person[key])


print(person.values())
for value in person.values():
    print(value)


print(person.items())
for item in person.items():
    print(f'{item[0]} = {item[1]}')