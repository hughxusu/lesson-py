class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

class ElectricCar(Car):
    def __init__(self, make, model, year):
        print('ElectricCar __init__')
    
my_tesla = ElectricCar('tesla', 'model s', 2024)
print(my_tesla.make)

# 打印继承链
print(ElectricCar.__mro__)