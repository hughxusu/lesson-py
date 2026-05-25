fn = lambda name, std_id, **kwargs: {'name': name, 'std_id': std_id, **kwargs}
print(fn('张三', '1001', phone='13800000000', is_active=False))
