students = [
    {'name': 'Tom', 'age': 20},
    {'name': 'Jack', 'age': 18},
    {'name': 'Mike', 'age': 22}
]

students.sort(key=lambda x: x['age'], reverse=True)
print(students)