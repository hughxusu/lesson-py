import re

pattern = r'hello'
s = 'hello hello'
result = re.match(pattern, s)
print(result)
print(type(result))

print(result.group())
print(result.start())
print(result.end())
print(result.span())
