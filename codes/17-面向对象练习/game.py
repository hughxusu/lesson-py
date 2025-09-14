import sys
import pygame as pg
from player import Player
from utils import Delay

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
        self.clock = pg.time.Clock()
        
        self.all_sprites = pg.sprite.Group()
        self.player = Player(360, 360)
        self.all_sprites.add(self.player)
        self.delay = Delay()

    def renew(self):
        self.delay.update()
        self.clock.tick(60)
        pg.display.update()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            
            keys = pg.key.get_pressed()
            self.all_sprites.update(keys)
            
            self.screen.fill((0, 0, 0))
            self.all_sprites.draw(self.screen)
            self.renew()

