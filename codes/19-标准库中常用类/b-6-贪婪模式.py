import re

# 贪婪模式
print(
    re.match(
        r'<div>.*</div>', '<div>Python</div><div>Regex</div>'
    ).group()
)

# 非贪婪模式
print(
    re.match(
        r'<div>.*?</div>', '<div>Python</div><div>Regex</div>'
    ).group()
)
