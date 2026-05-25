class TodoItem:
    def __init__(self, desc):
        self.__desc = self.__validate_desc(desc)
        self.__is_completed = False

    def toggle_completed(self):
        self.__is_completed = not self.__is_completed

    def show(self):
        status = '✅' if self.__is_completed else '⭕️'
        print(f'{status}  {self.__desc}')

    def __validate_desc(self, desc):
        if not isinstance(desc, str):
            desc = '无'
        if len(desc.strip()) == 0:
            desc = '无'
        if len(desc) > 100:
            desc = desc[:100]
        return desc

    def get_desc(self):
        return self.__desc

    def set_desc(self, desc):
        self.__desc = self.__validate_desc(desc)
        
item = TodoItem(123456)
item.__validate_desc('学习Python')