import re

result = re.compile(r'\d+')
print(result)
print(type(result))

src = 'a 123 b 456 c 789 d'

print(result.match(src))
print(result.search(src))
print(result.findall(src))
print(result.finditer(src))
print(result.split(src))
print(result.sub('-', src))
