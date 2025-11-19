from todoitem import TodoItem

class TodoList:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.__items = []
        self.__cmds = ['add', 'del', 'ok', 'undo', 'edit']

    def __parse_cmd(self, raw, is_cmd=True):
        tokens = raw.split(' ', 1)
        if is_cmd:
            if len(tokens) == 0:
                return None, None
            cmd = tokens[0]
            if cmd not in self.__cmds:
                return None, None
            return cmd, tokens[1:]
        else:
            if len(tokens) == 0:
                return None, None
            index = tokens[0].strip()
            if not index.isdigit():
                return None, None
            index = int(index) - 1
            if index < 0 or index >= len(self.__items):
                return None, None
            return index, tokens[1:]

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

    def __set_item_status(self, args, is_completed=True):
        if len(args) == 0 or args[0].strip() == '':
            print('请输入任务序号。')
        else:
            index = args[0].strip()
            if not index.isdigit():
                print('请输入正确的任务序号。')
            else:
                index = int(index) - 1
                if index < 0 or index >= len(self.__items):
                    print('任务序号不存在。')
                else:
                    self.__items[index].is_completed = is_completed
                    print(f'任务设置为{"完成" if is_completed else "未完成"}。')

    def __del_item(self, args):
        if len(args) == 0 or args[0].strip() == '':
            print('请输入任务序号。')
        else:
            index = args[0].strip()
            if not index.isdigit():
                print('请输入正确的任务序号。')
            else:
                index = int(index) - 1
                if index < 0 or index >= len(self.__items):
                    print('任务序号不存在。')
                else:
                    del self.__items[index]
                    print('任务删除成功。')

    def __edit_item(self, args):
        index, args = self.__parse_cmd(args[0], False)
        if index is None:
            print('请输入正确的任务序号。')
        else:
            if len(args) == 0 or args[0].strip() == '':
                print('请输入任务内容。')
            else:
                self.__items[index].desc = args[0].strip()
                print('任务修改成功。')

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
                elif cmd == 'ok':
                    self.__set_item_status(args)
                elif cmd == 'undo':
                    self.__set_item_status(args, False)
                elif cmd == 'del':
                    self.__del_item(args)
                elif cmd == 'edit':
                    self.__edit_item(args)
                else:
                    print('命令格式错误，请输入正确的命令。')