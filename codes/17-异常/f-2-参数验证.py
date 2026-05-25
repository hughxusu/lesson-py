def add_two_arr(first, second):
    assert len(first) == len(second), "输入数组长度必须相同"

    results = []
    for i, item in enumerate(first):
        result = item + second[i]
        results.append(result)
    return results

first = [1, 2, 3]
second = [1, 2, 3, 4]

try:
    print(add_two_arr(first, second))
except Exception as e:
    print(e)