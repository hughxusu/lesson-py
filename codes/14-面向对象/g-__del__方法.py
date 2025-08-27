class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def __del__(self):
        print('Car object is deleted!')
    
my_new_car = Car('audi', 'a4', 2019)
del my_new_car