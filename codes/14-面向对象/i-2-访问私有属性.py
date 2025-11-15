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
print(f'item.__is_completed: {item.__is_completed}')

# item.__is_completed = True