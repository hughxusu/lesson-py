class Car:
    def __init__(self):
        self.drive = 'front'
        
    def describe_car(self):
        print(f"This car has a {self.drive} drive.")
        
class ElectricCar(Car):
    def __init__(self):
        super().__init__()
        self.drive = 'rear'
        
    def describe_car(self):
        print(f"This electric car has a {self.drive} drive.")

    # 必须保证方法名和参数一致，否则会报错。
    # def describe_car(self, drive):
    #     print(f"This electric car has a {drive} drive.")
        
my_tesla = ElectricCar()
my_tesla.describe_car()