language = 'c and c++ and java and python and javascript and go'
print(language.startswith('c'))
print(language.startswith('c', 5, 20))

print(language.endswith('go'))
print(language.endswith('go', 5, 20))
print(language.endswith('go', -20, -11)) # 从右往左数，第一个字符是-1，第二个字符是-2，以此类推

print('hello'.isalpha())
print('hello '.isalpha())
print('hello#'.isalpha())
print('hello12345'.isalpha())

print('12345'.isdigit())
print('12345 '.isdigit())
print('12345#'.isdigit())
print('hello12345'.isdigit())

print('hello12345'.isalnum())
print('hello12345 '.isalnum())
print('hello12345#'.isalnum())

print('1 2 3 4 5'.isspace())
print('     '.isspace())