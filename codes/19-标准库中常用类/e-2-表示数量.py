import re

print(re.match(r'\D*', 'abc').group())
print(re.match(r'\d+', '123abc').group())
print(re.match('1[34578]\d{9}', '13144396831').group())
