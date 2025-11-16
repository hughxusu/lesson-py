class TodoList:
    def __new__(cls, *args, **kwargs):
        print('1. 创建实例__new__')
        return super().__new__(cls)

    def __init__(self):
        print('2. 初始化实例__init__')
        self.items = []

todo_list = TodoList()

