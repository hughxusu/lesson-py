choice = int(input('请输需要选择的功能序号: '))

if choice == 0:
    print('退出系统')
elif choice == 1:
    print('添加用户')
elif choice == 2:
    print('删除用户')

choice_map = {
    0: '退出系统',
    1: '添加用户',
    2: '删除用户',
}
print(choice_map[choice])