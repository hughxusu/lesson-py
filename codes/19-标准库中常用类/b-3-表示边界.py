import re

print(re.match(r'1[34578]\d{9}$', '13144396831').group())
print(re.match(r'\w+o\b', 'hello').group())
