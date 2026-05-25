def create_employee(name, **kwargs):
    print(kwargs)
    employee = {
        'name': name,
    }
    
    for key, value in kwargs.items():
        employee[key] = value

    return employee

employee = create_employee('Bob', age=25, job='dev', email='bob@example.com')
print(employee)
