choice = int(input('请输需要选择的功能序号: '))
if choice == 0:
    print('退出系统')
elif choice == 1:
    pass
elif choice == 2:
    pass
else:
    print('功能选择不存在')


day_number = int(input('请输今天是周几: '))
if day_number == 6 or day_number == 0:
    print('今天是休息日')
else:
    print('今天是工作日')


