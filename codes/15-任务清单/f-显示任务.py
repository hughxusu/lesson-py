class TodoItem:
    def __init__(self, desc):
        self.desc = desc
        self.is_completed = False

    def __str__(self):
        return f'{"✅" if self.is_completed else "⭕️"}-{self.desc}'

class TodoList:
    def __init__(self):
        self.__items = []
        self.__cmds = ['add', 'del', 'ok', 'undo', 'edit']

    def __parse_cmd(self, raw):
        tokens = raw.split(' ', 1)
        if len(tokens) == 0:
            return None, None
        cmd = tokens[0]
        if cmd not in self.__cmds:
            return None, None
        return cmd, tokens[1:]

    @staticmethod
    def __help():
        print('=' * 100)
        print('show 显示任务列表。')
        print('add [任务内容] 将任务添加到任务清单中。')
        print('del [index] 删除任务条目（index表示任务序号）。')
        print('ok [index] 设置任务为完成。')
        print('undo [index] 设置任务为未完成')
        print('edit [index] [任务内容] 修改任务的内容。')
        print('help 查询命令清单。')
        print('exit 退出系统。')
        print('=' * 100)

    def __short_info(self):
        print('-' * 100)
        print(f'当前任务数量{len(self.__items)}，操作命令如下：')
        print('show; exit; help; add [任务描述]; del [index]; ok [index]; undo [index]; edit [index] [任务内容]')
        print('=' * 100)

    def __add_item(self, args):
        if len(args) == 0 or args[0].strip() == '':
            print('请输入任务内容。')
        else:
            self.__items.append(TodoItem(args[0].strip()))
            print('任务添加成功。')

    def __show_items(self):
        print('=' * 100)
        if len(self.__items) == 0:
            print('当前任务列表为空。')
        else:
            for i, item in enumerate(self.__items, 1):
                print(f'{i}. {item}')
        self.__short_info()


    def run(self):
        print('=' * 100)
        print('欢迎使用任务清单')
        self.__short_info()
        while True:
            raw = input('').strip()
            if raw == 'exit':
                break
            elif raw == 'help':
                self.__help()
            elif raw == 'show':
                self.__show_items()
            else:
                cmd, args = self.__parse_cmd(raw)
                if cmd == 'add':
                    self.__add_item(args)
                else:
                    print('命令格式错误，请输入正确的命令。')

todo_list = TodoList()
todo_list.run()

