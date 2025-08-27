class Dog:
    def __init__(self, name):
        self.name = name
        print(f'instance is {id(self)}')
        
    def sit(self):
        print(f'instance is {id(self)}')
        print(self.name.title() + " is now sitting.")
    
dog_tom = Dog('tom')
dog_will = Dog('will')

print(id(dog_tom))
print(id(dog_will))

dog_tom.sit()
dog_will.sit()

tom = dog_tom
print(tom is dog_tom)
print(tom is dog_will)

a = 3
b = 3
print(a is b)

a = 1000
b = 1000
print(a is b) 
print(a == b)