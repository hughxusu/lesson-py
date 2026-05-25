a = set([1, 2])
b = set([2, 3])
inter = a & b
union = a | b
minus = a - b
diff = a ^ b

print(a)
print(b)
print(f"inter: {inter}")
print(f"union: {union}")
print(f"minus: {minus}")
print(f"diff: {diff}")