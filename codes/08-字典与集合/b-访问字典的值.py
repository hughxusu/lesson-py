person = {
  'name': 'Bob',
  'age': 25,
  'job': 'Dev',
  'city': 'New York',
  'email': 'bob@web.com'
}


print(person['name'])
print(person['is_male']) # 获取值报错


print(person.get('job', 'Manager'))
print(person.get('is_male', True))