import vehicle.car
import vehicle.sub_cars

audi = vehicle.car.Car('audi', 'a4', 2019)
print(audi.get_descriptive_name())
tesla = vehicle.sub_cars.ElectricCar('tesla', 'model s', 2019)
print(tesla.get_descriptive_name())
li = vehicle.sub_cars.HybridCar('Li', 'L7', 2023)
print(li.get_descriptive_name())