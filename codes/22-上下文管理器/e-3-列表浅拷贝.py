import copy

my_list1 = [1, 3, [4, 6]]
my_list2 = copy.copy(my_list1)
print("my_list1:", id(my_list1))
print("my_list2:", id(my_list2))
