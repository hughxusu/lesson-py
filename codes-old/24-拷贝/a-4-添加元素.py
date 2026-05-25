import copy

my_list1 = [1, 3, [4, 6]]
my_list2 = copy.copy(my_list1)
my_list2.append(5)
print("my_list1:", my_list1)
print("my_list2:", my_list2)
