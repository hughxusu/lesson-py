class Car:
    def __init__(self):
        print('Car __init__')
        
class ElectricCar(Car):
    def __init__(self):
        super().__init__()
        print('ElectricCar __init__')
        
class GasCar(Car):
    def __init__(self):
        super().__init__()
        print('GasCar __init__')
        
class HybridCar(ElectricCar, GasCar):
    def __init__(self):
        super().__init__()
        print('HybridCar __init__')
        
print(HybridCar.__mro__)