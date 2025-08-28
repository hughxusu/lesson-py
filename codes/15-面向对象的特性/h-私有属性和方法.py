class Car:
    def __init__(self):
        self.__color = 'white'
        
    def __update_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__update_color(color)
        
my_car = Car()
print(my_car.__color)
my_car.__update_color('red')

# 读取或写入私有属性
# my_car = Car()
# print(my_car.get_color())
# my_car.set_color('red')
# print(my_car.get_color())

class ElectricCar(Car):
    def __init__(self):
        super().__init__()
        
    def describe_color(self):
        print(f"This car is {self.__color}.")
        
    def change_color(self, color):
        self.__update_color(color)
        
my_car = ElectricCar()
my_car.describe_color()     
my_car.change_color('red')  