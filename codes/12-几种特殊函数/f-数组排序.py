students = [
    {'name': 'Tom', 'age': 20},
    {'name': 'Jack', 'age': 18},
    {'name': 'Mike', 'age': 22}
]

# 按age值升序排列
students.sort(key=lambda x: x['age'])
print(students)

# 按age值降序排列
students.sort(key=lambda x: x['age'], reverse=True)
print(students)