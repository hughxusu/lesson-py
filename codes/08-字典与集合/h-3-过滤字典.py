# 字典中提取
stocks = {'apple': 268, 'google': 218, 'twitter': 122, 'facebook': 153, 'tesla': 230}
better = {key: value for key, value in stocks.items() if value >= 200}
print(better)