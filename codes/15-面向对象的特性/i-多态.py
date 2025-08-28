class Car:
    def run(self):
        pass
    
class ElectricCar(Car):
    def run(self):
        print('Electric car is running silently.')
        
class GasCar(Car):
    def run(self):
        print('Gas car is running fast.')
        
class Driver:
    def __init__(self, car):
        self.car = car

    def drive(self):
        self.car.run()
        
tesla = ElectricCar()
audi = GasCar()
driver = Driver(tesla)
driver.drive()
driver = Driver(audi)
driver.drive()

# 判断是否是某个类的实例
print(isinstance(tesla, ElectricCar))
print(isinstance(tesla, Car))
print(isinstance(tesla, GasCar))
print(isinstance(tesla, object))