# 1. 定义外部函数
def multiplier_factory(factor):
    
    # 2. 定义内部函数
    def multiplier(number):
        return number * factor
    
    # 3. 外部函数返回了内部函数
    return multiplier

# 创建两个不同的乘法器
double = multiplier_factory(2)
triple = multiplier_factory(3)

print(double(5))  # 输出: 10
print(triple(5))  # 输出: 15