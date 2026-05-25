import math

def distance(x1, x2):
    if len(x1) != len(x2):
        raise ValueError("x1和x2的长度不一致")

    sum = 0
    for i in range(len(x1)):
        sum += (x1[i] - x2[i]) ** 2
    return math.sqrt(sum)