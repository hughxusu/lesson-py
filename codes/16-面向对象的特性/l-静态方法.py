class Car:
    total_cars = 0 
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    @staticmethod
    def calculate_distance(arrival):
        print(f'Calculate distance to {arrival}')
        
audi = Car('audi', 'a4', 2020)
audi.calculate_distance('home')
Car.calculate_distance('home')