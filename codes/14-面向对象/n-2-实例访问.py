class TodoItem:
    item_count = 0

    def __init__(self, desc):
        self.desc = desc
        self.is_completed = False
        TodoItem.item_count += 1

    def __str__(self):
        return f'{"✅" if self.is_completed else "⭕️"}  {self.desc}'

item1 = TodoItem('学习Python')
item1.item_count = 10
print(f'item1.item_count: {item1.item_count}')
item2 = TodoItem('学习JavaScript')
print(f'item2.item_count: {item2.item_count}')
print(f'TodoItem.item_count: {TodoItem.item_count}')




