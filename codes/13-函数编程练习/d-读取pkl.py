import pickle

f = open('汽车.pkl', 'rb')
cars = pickle.load(f)
f.close()
print(cars)
print(type(cars))
print(type(cars[0]))