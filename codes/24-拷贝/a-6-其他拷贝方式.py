my_list1 = [1, 3, [4, 6]]
my_list2 = my_list1[:]
print("my_list1:", id(my_list1))
print("my_list2:", id(my_list2))

my_list2.append(5)
print("my_list1:", my_list1)
print("my_list2:", my_list2)

my_list2[2].append(8)
print("my_list1:", my_list1)
print("my_list2:", my_list2)
