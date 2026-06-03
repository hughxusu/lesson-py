day_number = int(input('请输今天是周几: '))
if day_number >= 1 and day_number <= 5:
    print('今天是工作日')
else:
    print('今天是休息日')