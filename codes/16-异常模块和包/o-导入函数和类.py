from vehicle.car import Car
from vehicle.sub_cars import ElectricCar, HybridCar

audi = Car('audi', 'a4', 2019)
print(audi.get_descriptive_name())
tesla = ElectricCar('tesla', 'model s', 2019)
print(tesla.get_descriptive_name())
li = HybridCar('Li', 'L7', 2023)
print(li.get_descriptive_name())