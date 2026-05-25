import re

# 表示任意字符
print(re.match(r'.', 'a').group())
print(re.match(r'...', 'xyz').group())

# 表示任意数字
print(re.match(r'\d', '1').group())

# 表示任意非数字字符
print(re.match(r'\D', 'a').group())

# 表示a-z和5-9范围内取
print(re.match('[a-z5-9]', 'a8').group())

