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

ret = re.match(
    "<(?P<name1>[a-zA-Z1-6]+)><(?P<name2>[a-zA-Z1-6]+)>.*</(?P=name2)></(?P=name1)>", 
    "<html><h1>www.apple.cn</h1></html>"
)
print(ret.group())
print(ret.group('name1'))
print(ret.group('name2'))
