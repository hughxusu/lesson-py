even_sum = 0

i = 0
while i <= 100:
    if i % 2 == 0:
        even_sum += i
    i += 1 # i+=2 可以控制增量为2改写代码
print(f"0~100之间偶数和为{even_sum}")