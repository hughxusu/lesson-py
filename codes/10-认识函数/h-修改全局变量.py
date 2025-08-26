pi = 3.14

def circle():
    print(pi)

circle()
print(f'全局变量 pi = {pi}')

def area():
    pi = 3.1415926
    print(pi)

area()
print(f'全局变量 pi = {pi}')