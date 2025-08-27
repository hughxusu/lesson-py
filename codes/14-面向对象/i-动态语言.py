class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
      
my_new_car = Car('audi', 'a4', 2019)
my_new_car.color = 'red'
print(my_new_car.color)

# byd = Car('byd', 'seal', 2020)
# print(byd.color)