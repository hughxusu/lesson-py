class TodoItem:
    def __init__(self, desc):
        self.desc = desc
        self.is_completed = False

    def show(self):
        status = '✅' if self.is_completed else '⭕️'
        print(f'{status}  {self.desc}')

    def __eq__(self, other):
        if not isinstance(other, TodoItem):
            return False
        return self.desc == other.desc and self.is_completed == other.is_completed
    
item_1 = TodoItem('学习Python')
item_2 = TodoItem('学习Python')
item_3 = item_1
print(f'item_3 == item_1: {item_3 == item_1}')
print(f'item_3 == item_2: {item_3 == item_2}')

