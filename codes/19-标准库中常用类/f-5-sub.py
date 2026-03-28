import re

result = re.sub(r'\s+', '-', 'a  b c d', count=2)
print(result)