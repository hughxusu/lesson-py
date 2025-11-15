class TodoItem:
    item_count = 0

    def __init__(self, desc):
        self.desc = desc
        self.is_completed = False
        TodoItem.item_count += 1

    def __str__(self):
        return f'{'✅' if self.is_completed else '⭕️'}  {self.desc}'

item1 = TodoItem('学习Python')
item2 = TodoItem('学习JavaScript')
print(f'当前待办事项数量: {TodoItem.item_count}')

