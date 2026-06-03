person = {
  'name': 'Bob',
  'age': 25,
  'job': 'Dev',
  'city': 'New York',
  'email': 'bob@web.com'
}

print(person.items())
print('-'*50)
for item in person.items():
    print(f'{item[0]} = {item[1]}')