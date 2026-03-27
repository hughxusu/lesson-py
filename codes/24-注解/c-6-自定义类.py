from __future__ import annotations

class TodoItem:
    def __init__(self, desc: str):
        self.desc = desc
        self.is_completed: bool = False

    def __str__(self):
        return f'{"✅" if self.is_completed else "⭕️"}-{self.desc}'

    @classmethod
    def from_dict(cls, item_dict: dict[str, str | bool]) -> TodoItem:
        item = cls(str(item_dict['desc']))
        item.is_completed = bool(item_dict['is_completed'])
        return item

    
class TodoList:
    def __init__(self):
        self.__items: list[TodoItem] = []