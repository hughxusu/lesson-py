pi = 3.14

def area():
    global pi
    pi = 3.1415926
    print(pi)

area()
print(f'全局变量 pi = {pi}')