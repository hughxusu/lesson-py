def round_area(r):
    return 3.14 * r ** 2

def cylinder(r, h):
    return round_area(r) * h

def circular_cone(r, h):
    return cylinder(r, h) / 3

print(round_area(5))
print(cylinder(5, 10))
print(round_area(10) - round_area(5))