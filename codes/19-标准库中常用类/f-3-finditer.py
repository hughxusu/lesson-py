import re

result = re.finditer(r'\d+', 'hello 12345 6789')
print(result)
for item in result:
    print(item)