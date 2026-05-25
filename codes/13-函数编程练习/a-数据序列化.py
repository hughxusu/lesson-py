import json

cars = [
    {'make': 'audi', 'model': 'a4', 'year': 2019},
    {'make': 'bmw', 'model': 'm3', 'year': 2020},
]

f = open('cars.json', 'w', encoding='utf-8')
json.dump(cars, f)
f.close()
