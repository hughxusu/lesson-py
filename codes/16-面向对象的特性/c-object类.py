class Car(object):
    def __init__(self, make, model, year):
        print('Car __init__')
        
print(Car.__mro__)