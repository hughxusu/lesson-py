pi = 3.1415926 

def round_area(r):
    pi = 3.14
    area = pi * r ** 2
    return area

result = round_area(1)
print(f'半径为5的圆的面积是: {result}')
print(f'全局变量 pi = {pi}')