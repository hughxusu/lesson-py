from car import Car, ElectricCar

audi = Car('audi', 'a4', 2019)
print(audi.get_descriptive_name())
tesla = ElectricCar('tesla', 'model s', 2019)
print(tesla.get_descriptive_name())

print(f'my_cars.py __name__={__name__}')