from collections import Counter

colors_one = ['red', 'green', 'blue', 'green']
cnt_one = Counter(colors_one)
print(cnt_one)
print(f"green 出现了 {cnt_one['green']}")

colors_two = ['red', 'yellow', 'green']
cnt_two = Counter(colors_two)
print(cnt_two)

print(f"并集: {cnt_one + cnt_two}")
print(f"差集: {cnt_one - cnt_two}")
print(f"交集: {cnt_one & cnt_two}")
print(f"并集: {cnt_one | cnt_two}")
