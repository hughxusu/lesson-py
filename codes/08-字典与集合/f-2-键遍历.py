person = {
  'name': 'Bob',
  'age': 25,
  'job': 'Dev',
  'city': 'New York',
  'email': 'bob@web.com'
}

print(person.keys()) # 可迭代对象类似于数组
print('-'*50)
for key in person.keys():
    print(person[key])