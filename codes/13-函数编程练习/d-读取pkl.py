import pickle

f = open('cars.pkl', 'rb')
cars = pickle.load(f)
f.close()
print(cars)
print(type(cars))
print(type(cars[0]))