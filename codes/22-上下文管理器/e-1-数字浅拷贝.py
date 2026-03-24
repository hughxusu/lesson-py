import copy

num1 = 1
num2 = copy.copy(num1)
print("num1:", id(num1))
print("num2:", id(num2))
