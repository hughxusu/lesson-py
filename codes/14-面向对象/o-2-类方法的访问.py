class TodoItem:
    item_count = 0

    def __init__(self, desc):
        self.desc = desc
        self.is_completed = False
        TodoItem.item_count += 1

    def __str__(self):
        return f'{'✅' if self.is_completed else '⭕️'}  {self.desc}'

    @classmethod
    def get_item_count(cls):
        return cls.item_count

    @classmethod
    def set_item_count(cls, count):
        cls.item_count = count


item1 = TodoItem('学习Python')
TodoItem.set_item_count(10)
print(f'item1.get_item_count: {item1.get_item_count()}')
print(f'TodoItem.item_count: {TodoItem.item_count}')




