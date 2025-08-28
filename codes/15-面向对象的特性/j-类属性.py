class Car:
    number_of_wheels = 4
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

audi = Car('audi', 'a4', 2020)
print(audi.number_of_wheels)
bmw = Car('bmw', 'x5', 2020)
print(bmw.number_of_wheels)

tesla = ElectricCar('tesla', 'model s', 2020)
print(tesla.number_of_wheels)

# 修改类属性
Car.number_of_wheels = 6
print(audi.number_of_wheels)
print(bmw.number_of_wheels)
print(tesla.number_of_wheels)

# 创建一个实例属性
audi.number_of_wheels = 4
print(audi.number_of_wheels)
print(bmw.number_of_wheels)
print(tesla.number_of_wheels)