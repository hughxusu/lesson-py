def get_average(arr):
    '''
    计算数组的平均值
    :param arr: 输入的数组
    :return: 数组的平均值
    '''
    sum = 0
    for i in arr:
        sum += i
    avg = sum / len(arr)
    return avg

help(get_average)
