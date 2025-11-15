def create_student(name, std_id, email=None, phone=None, is_active=True):
    student = {
        'name': name,
        'std_id': std_id,
        'email': email, 
        'phone': phone,
        'is_active': is_active,
    }
    return student
student = create_student('张三', '1001', 'zhangsan@example.com')
print(student)


