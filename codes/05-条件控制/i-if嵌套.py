in_str = input('请输需要选择的功能序号: ')
if in_str.isdigit():
    choice = int(in_str)
    if choice == 0:
        print('退出系统')
    elif choice == 1:
        print('添加用户')
    elif choice == 2:
        print('删除用户')
else:
    print('输入的不是数字')