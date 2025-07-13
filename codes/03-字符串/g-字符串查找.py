language = 'c and c++ and java and python and javascript and go'
print(language.find('and'))
print(language.find('and', 15, 30))
print(language.find('c#'))


print(language.index('and'))
print(language.index('and', 15, 30))
print(language.index('c#'))


print(language.rfind('go'))
print(language.rindex('go'))


print(language.count('and'))
print(language.count('and', 15, 30))
print(language.count('c#'))