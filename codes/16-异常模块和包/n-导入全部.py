from car import *

audi = Car('audi', 'a4', 2019)
print(audi.get_descriptive_name())
tesla = ElectricCar('tesla', 'model s', 2019) # 导入报错
print(tesla.get_descriptive_name())