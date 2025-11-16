class TodoItem:
    def __init__(self, desc):
        self.desc = desc
        self.is_completed = False

    def __str__(self):
        return f'{"✅" if self.is_completed else "⭕️"}  {self.desc}'


class TodoList:
    def __init__(self):
        self.items = []

    def run(self):
        while True:
            raw = input('')
            if raw == 'exit':
                break
            else:
                print(raw)

todo_list = TodoList()
todo_list.run()

