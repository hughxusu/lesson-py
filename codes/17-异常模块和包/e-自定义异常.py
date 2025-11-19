class NotSameLengthError(Exception):
    def __init__(self):
        super().__init__(self)

    def __str__(self):
        return '输入数组长度必须相同'


def add_two_arr(first, second):
    if len(first) != len(second):
        raise NotSameLengthError()

    results = []
    for i in first:
        result = first[i] + scond[i]
        results.append(result)
    return results

first = [1, 2, 3]
second = [1, 2, 3, 4]

try:
    add_two_arr(first, second)
except NotSameLengthError as e:
    print(e)