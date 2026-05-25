class TodoList:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            inst = super().__new__(cls)
            cls.__instance = inst
        return cls.__instance

    def __init__(self):
        self.__items = []
        self.__cmds = ['add', 'del', 'ok', 'undo', 'edit']

todo1 = TodoList()
todo2 = TodoList()
print(f'todo1 id: {id(todo1)}, todo2 id: {id(todo2)}')
print(todo1 is todo2)
