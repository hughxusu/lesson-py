from vehicle.car import Car

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

class GasCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.gas = 50

    def describe_gas(self):
        print(f"This car has a {self.gas} L gas.")

class HybridCar(ElectricCar, GasCar):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 30
        self.gas = 40