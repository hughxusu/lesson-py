# __all__ = ['TodoItem']

class TodoItem:
    def __init__(self, desc):
        self.desc = desc
        self.is_completed = False

    def __str__(self):
        return f'{"✅" if self.is_completed else "⭕️"}-{self.desc}'

    @classmethod
    def from_dict(cls, item_dict):
        item = cls(item_dict['desc'])
        item.is_completed = item_dict['is_completed']
        return item

# item = TodoItem('学习Python')
# print(item)
# item.is_completed = True
# print(item)

# print(f'todoItem.py = {__name__}')

if __name__ == '__main__':
    item = TodoItem('学习Python')
    print(item)
    item.is_completed = True
    print(item)

