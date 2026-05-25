f = open('出塞.txt', 'r')
while line := f.readline():
    print(line, end='')
f.close()
