def avg(*args):
    print(args)
    if len(args) == 0:
        return None

    sum = 0
    for i in args:
        sum += i
    avg = sum / len(args)
    return avg

result = avg(1, 2, 3, 4, 5)
print(result)