class Car:
    def __new__(cls, *args, **kwargs):
        print('Creating instance')
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
audi = Car('audi', 'a4', 2020)    