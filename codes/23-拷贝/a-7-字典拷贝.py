old_dict = {'a': 1, 'b': [11, 22]}
new_dict = old_dict.copy()

print("old_dict:", id(old_dict))
print("new_dict:", id(new_dict))

old_dict['b'].append(33)
print("old_dict:", old_dict)
print("new_dict:", new_dict)
