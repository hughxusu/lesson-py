import copy

num1 = 1
num2 = copy.copy(num1)
print("num1:", id(num1), "num2:", id(num2))

my_tuple1 = (3, 5)
my_tuple2 = copy.copy(my_tuple1)
print("my_tuple1:", id(my_tuple1), "my_tuple2:", id(my_tuple2))


my_list1 = [1, 3, [4, 6]]
my_list2 = copy.copy(my_list1)
print("my_list1:", id(my_list1), "my_list2:", id(my_list2))

my_list1.append(5)
print(my_list1, my_list2)
print("my_list1[2]:", id(my_list1[2]), "my_list2[2]:", id(my_list2[2]))

my_list1[2].append(3)
print(my_list1, my_list2)