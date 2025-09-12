import pygame as pg
import sys
from player import Player  # 导入Player类

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
        self.player = Player(360, 360)  # 在屏幕中心创建玩家
        self.all_sprites.add(self.player)
        self.delay = 100

    def run(self):
        while True:
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            
            keys = pg.key.get_pressed()
            self.all_sprites.update(keys)
            
            self.screen.fill((0, 0, 0))
            self.all_sprites.draw(self.screen)
            
            self.clock.tick(60)

            self.delay -= 1
            if not self.delay:
                self.delay = 100

            print(self.delay)

