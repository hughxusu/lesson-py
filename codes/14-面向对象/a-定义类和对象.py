class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sit(self):
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6)
print(type(my_dog))
print(my_dog)

# 实例属性
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# 实例方法
my_dog.sit()
my_dog.roll_over()
