import pygame as pg
import sys


class Game:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((720, 720))
        pg.display.set_caption('Tank fight!')


    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    
            pg.display.update()