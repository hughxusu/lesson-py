class Car:
    total_cars = 0 
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Car.total_cars += 1 # 每创建一个实例，计数器加1
        
    @classmethod
    def cars_created(cls):
        return cls.total_cars
    
audi = Car('audi', 'a4', 2020)
bmw = Car('bmw', 'x5', 2020)

print(Car.cars_created())
print(audi.cars_created())
print(bmw.cars_created())