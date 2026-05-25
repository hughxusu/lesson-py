class TodoItem:
    def __init__(self, desc):
        self.desc = desc
        self.__is_completed = False

    def toggle_completed(self):
        self.__is_completed = not self.__is_completed

    def show(self):
        status = '✅' if self.__is_completed else '⭕️'
        print(f'{status}  {self.desc}')

item = TodoItem('学习Python')
item.show()
item.toggle_completed()
item.show()