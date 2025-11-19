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

# 打印 __name__
# print(f'todoitem.py is {__name__}')

# 测试方法
# if __name__ == '__main__':
#     item = TodoItem('学习Python')
#     print(item)
