def avg(items: list[int]) -> float:
    total = 0
    count = 0
    for item in items:
        total += item
        count += 1
    return total / count

reuslt = avg((1, 2, 3))
print(reuslt)