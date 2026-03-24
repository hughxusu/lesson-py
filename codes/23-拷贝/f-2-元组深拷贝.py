import copy

my_tuple1 = (1, [1, 2])
my_tuple2 = copy.deepcopy(my_tuple1)
print("my_tuple1:", id(my_tuple1))
print("my_tuple2:", id(my_tuple2))
