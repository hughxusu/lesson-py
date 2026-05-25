import copy

num1 = 1
num2 = copy.deepcopy(num1)
print("num1:", id(num1))
print("num2:", id(num2))

my_tuple1 = (1, 2)
my_tuple2 = copy.deepcopy(my_tuple1)
print("my_tuple1:", id(my_tuple1))
print("my_tuple2:", id(my_tuple2))