class TodoItem:
    def __init__(self, desc):
        self.desc = self.validate_desc(desc)
        self.is_completed = False

    def show(self):
        status = '✅' if self.is_completed else '⭕️'
        print(f'{status}  {self.desc}')

    @staticmethod
    def validate_desc(desc):
        if not isinstance(desc, str):
            desc = '无'
        if len(desc.strip()) == 0:
            desc = '无'
        if len(desc) > 100:
            desc = desc[:100]
        return desc
        
item = TodoItem(123456)
item.show()
print(TodoItem.validate_desc(''))