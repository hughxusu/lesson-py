my_list = [1, 2, 3]
my_iter = iter(my_list)

while True:
    try:
        result = next(my_iter)
        print(f'当前元素为: {result}')
    except StopIteration as e:
        break

    # result = next(my_iter)
    # print(f'当前元素为: {result}')