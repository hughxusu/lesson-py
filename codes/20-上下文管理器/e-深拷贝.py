import copy

num1 = 1
num2 = copy.deepcopy(num1)
print("num1:", id(num1), "num2:", id(num2))

str1 = 'hello'
str2 = copy.deepcopy(str1)
print("str1:", id(str1), "str2:", id(str2))

my_tuple1 = (1, [1, 2])
my_tuple2 = copy.deepcopy(my_tuple1)
print("my_tuple1:", id(my_tuple1), "my_tuple2:", id(my_tuple2))
print("my_tuple1[1]:", id(my_tuple1[1]), "my_tuple2[1]:", id(my_tuple2[1]))

my_tuple2[1].append(4)
print(my_tuple1, my_tuple2)
print("my_tuple1[0]:", id(my_tuple1[0]), "my_tuple2[0]:", id(my_tuple2[0]))

my_list1 = [1, [2, 3]]
my_list2 = copy.deepcopy(my_list1)
print("my_list1:", id(my_list1), "my_list2:", id(my_list2))
print("my_list1[1]:", id(my_list1[1]), "my_list2[1]:", id(my_list2[1]))