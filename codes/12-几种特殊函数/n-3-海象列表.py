data = [5, 12, 8, 15]
results = [y for x in data if (y := x*x) > 100]
print(results)