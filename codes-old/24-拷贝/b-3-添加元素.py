import copy

my_list1 = (1, [1, 2])
my_list2 = copy.deepcopy(my_list1)
print("my_list1:", my_list1)
print("my_list2:", my_list2)

my_list2[1].append(5)
print("my_list1:", my_list1)
print("my_list2:", my_list2)
