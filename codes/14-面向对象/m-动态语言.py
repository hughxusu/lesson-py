class TodoItem:
    def __init__(self, desc):
        self.desc = desc
        self.is_completed = False

    def __str__(self):
        return f'{"✅" if self.is_completed else "⭕️"}  {self.desc}'

item1 = TodoItem('学习Python')
item1.note = '需要先学习基础语法'
print(item1.note)

# item2 = TodoItem('学习JavaScript')
# print(item2.note)

