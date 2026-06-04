f = open('凉州词.txt', 'r')
while line := f.readline():
    print(line, end='')
    print('-' * 20)
f.close()
