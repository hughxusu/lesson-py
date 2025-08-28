from vehicle import car, sub_cars

audi = car.Car('audi', 'a4', 2019)
print(audi.get_descriptive_name())
tesla = sub_cars.ElectricCar('tesla', 'model s', 2019)
print(tesla.get_descriptive_name())
li = sub_cars.HybridCar('Li', 'L7', 2023)
print(li.get_descriptive_name())