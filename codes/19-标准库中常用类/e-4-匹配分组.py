import re

# 匹配0-100之间的数字
print(re.match(r'[1-9]\d?$|0$|100$', '88').group())

# 匹配邮箱
print(
    re.match(
        r'\w+@(163|126|gmail|qq).(com|cn|net)$', 
        'tommy@qq.com'
    ).group()
)
