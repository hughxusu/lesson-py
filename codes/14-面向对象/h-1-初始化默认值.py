class TodoItem:
    def __init__(self, desc='无'):
        self.desc = desc
        self.is_completed = False

item = TodoItem()
print(f'item->desc: {item.desc}')
