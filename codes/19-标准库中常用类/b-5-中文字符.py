import re

# 中文匹配
print(
    re.match(
        r'[\u4e00-\u9fa5]{5}', '青山横北郭，白水绕东城。'
    ).group()
)
