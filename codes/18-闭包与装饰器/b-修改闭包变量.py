def make_counter(init=0):
    count = init  # 外层函数的局部变量
    
    def counter():
        nonlocal count  # 使用 nonlocal 声明外层变量
        count += 1
        return count
    
    return counter

# 创建一个计数器实例
my_counter = make_counter()

print(my_counter())  
print(my_counter())  
print(my_counter())  

# 创建另一个计数器实例
another_counter = make_counter(10)

print(another_counter())  
print(another_counter()) 