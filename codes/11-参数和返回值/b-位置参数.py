def subtract_list(first, second):
    if len(first) != len(second):
        return None

    result = []

    for i in range(len(first)):
        result.append(first[i] - second[i])
    return result

a = [1, 2, 3]
b = [4, 5, 6]

result = subtract_list(first=b, second=a)
print(result)

# result = subtract_list(second=a, first=b)
# print(result)

# result = subtract_list(b, second=a)
# print(result)