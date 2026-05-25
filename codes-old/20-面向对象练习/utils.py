import pygame as pg

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
BULLET_COOL_DOWN = 200


def get_screen_rect():
    return pg.display.get_surface().get_rect()


class Delay:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.count = 100

    def update(self):
        self.count -= 1

        if not self.count:
            self.count = 100

