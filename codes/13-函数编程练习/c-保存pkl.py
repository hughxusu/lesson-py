import pickle

cars = [
    {'make': 'audi', 'model': 'a4', 'year': 2019},
    {'make': 'bmw', 'model': 'm3', 'year': 2020},
]

f = open('汽车.pkl', 'wb')
pickle.dump(cars, f)
f.close()
