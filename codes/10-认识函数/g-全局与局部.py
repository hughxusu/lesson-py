# 全局变量
pi = 3.1415926 

def round_area(r):
    # 局部变量
    area = pi * r ** 2
    return area

result = round_area(5)
print(f'半径为5的圆的面积是: {result}')
# print(area)
