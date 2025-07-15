numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
sites = ('Google', 'Runoob', 'Wiki', 'Taobao', 'Wiki', 'Weibo', 'Weixin')
message = 'hello, python'

numbers_t = tuple(numbers)
print(numbers_t)
print(type(numbers_t))

sites_l = list(sites)
print(sites_l)
print(type(sites_l))

message_l = list(message)
print(message_l)
print(type(message_l))

# 等价于 numbers_s = '[10, 20, 30, 40, 50, 60, 70, 80, 90]'
numbers_s = str(numbers)
print(numbers_s)
print(type(numbers_s))

sites_set = set(sites) # 可以对数据进行去重
message_set = set(message)
print(sites_set)
print(type(sites_set))
print(message_set)