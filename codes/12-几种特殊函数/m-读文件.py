# read
f = open('docs.txt', 'r')
txt = f.read()
print(txt)
f.close()

# readlines
f = open('docs.txt', 'r')
lines = f.readlines()
print(lines)
f.close()

# readline
f = open('docs.txt', 'r')

line = f.readline()
print(line)

line = f.readline()
print(line)

f.close()