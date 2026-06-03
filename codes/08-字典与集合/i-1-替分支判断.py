choice = int(input('请输需要选择的功能序号: '))

choice_map = {
    0: '退出系统',
    1: '添加用户',
    2: '删除用户',
}
print(choice_map[choice])