def get_average(arr):
    sum = 0
    for i in arr:
        sum += i
    avg = sum / len(arr)
    return avg

a = [6.5, 7, 8, 7]
avg = get_average(a)
print(f'平均值是: {avg}')

# b = [9.5, 7.5, 8, 8, 7]
# avg = get_average(b)
# print(f'平均值是: {avg}')
