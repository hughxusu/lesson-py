import json

f = open('汽车.json', 'r', encoding='utf-8')
cars = json.load(f)
f.close()
print(cars)
print(type(cars))
print(type(cars[0]))