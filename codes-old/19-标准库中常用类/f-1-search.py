import re

result = re.search(r'白水', '青山横北郭，白水绕东城。')
print(type(result))
print(result.group())

result = re.search(r'^白水', '青山横北郭，白水绕东城。')
print(result)