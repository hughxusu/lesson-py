language = 'c and c++ and java and python and javascript and go'
replace = language.replace('and', '&')
print(language)
print(replace)
print(language.replace('and', '&', 2))

print(language.split('and'))
print(language.split(' '))
print(language.split('and', 2))

langs = language.split(' ')
print('_'.join(langs))

print(language.capitalize())
print(language.title())
print(language.lower())
print(language.upper())

language = '				c and c++ and java and python and javascript and go				'
print(language)
print(language.lstrip())
print(language.rstrip())
print(language.strip())