class TodoItem:
    def __init__(self, desc):
        self.desc = desc
        self.is_completed = False

    def show(self):
        status = '✅' if self.is_completed else '⭕️'
        print(f'{status}  {self.desc}')

item = TodoItem('学习Python')
item.show()
