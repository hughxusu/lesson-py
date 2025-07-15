numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
sites = ('Google', 'Runoob', 'Wiki', 'Taobao', 'Wiki', 'Weibo', 'Weixin')
message = 'hello, python'

# 字符串也支持索引操作
print(message[1])
print(message[-1])


sub = numbers[2:7]
print(sub)
print(type(sub))


sub_c = sites[2:7]
print(sub_c)
print(type(sub_c))

sub_m = message[2:7]
print(sub_m)
print(type(sub_m))


sub = numbers[:7]
print(sub)

sub = numbers[2:]
print(sub)

sub = numbers[2:7:2]
print(sub)


sub = numbers[-6:-2]
print(sub)

sub = numbers[::-1] # 数组逆序
print(sub)