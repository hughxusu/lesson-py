class TodoItem:
    def __init__(self, desc):
        self.desc = desc
        self.is_completed = False

    def toggle_completed(self):
        self.is_completed = not self.is_completed

    def show(self):
        status = '✅' if self.is_completed else '⭕️'
        print(f'{status}  {self.desc}')

item = TodoItem('学习Python')
item.is_completed = True
item.show()
item.toggle_completed()
item.show()
