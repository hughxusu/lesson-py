def round_area(r):
    return 3.14 * r ** 2

def cylinder(r, h):
    return round_area(r) * h

print(f'半径为5的圆的面积是: {round_area(5)}')
print(f'半径为5, 高为10的圆柱体体积是: {cylinder(5, 10)}')