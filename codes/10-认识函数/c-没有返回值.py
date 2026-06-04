def get_average(arr):
    sum = 0
    for i in arr:
        sum += i
    avg = sum / len(arr)
    print(f'平均值是: {avg}')
    

a = [6.5, 7, 8, 7]
avg = get_average(a)
print(f'返回值为: {avg}')