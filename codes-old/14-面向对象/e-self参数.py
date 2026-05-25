class TodoItem:
    def __init__(self, desc):
        self.desc = desc
        self.is_completed = False
        print(f'__init__的self的id为{id(self)}')

    def show(self):
        status = '✅' if self.is_completed else '⭕️'
        print(f'{status}  {self.desc}')
        print(f'show的self的id为{id(self)}')

item = TodoItem('学习Python')
item.show()
print(f'item的id为{id(item)}')