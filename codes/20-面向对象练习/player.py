import pygame as pg
import utils
from utils import Delay
from bullet import Bullet

TANK_IMG = r"images/tank_T1_0.png"

class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.tank = pg.image.load(TANK_IMG).convert_alpha()
        self.direction = None
        self.set_direction_image(utils.UP)
        self.image = self.tank_R0

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        self.delay = Delay()
        self.last_fire_time = 0
       

    def switch_image(self):
        if self.delay.count % 5 == 0:
            self.image = self.tank_R1 if self.image == self.tank_R0 else self.tank_R0


    def set_direction_image(self, d):
        if self.direction != utils.UP and d == utils.UP:
            self.tank_R0 = self.tank.subsurface((0, 0), (48, 48))
            self.tank_R1 = self.tank.subsurface((48, 0), (48, 48))
        elif self.direction != utils.DOWN and d == utils.DOWN:
            self.tank_R0 = self.tank.subsurface((0, 48), (48, 48))
            self.tank_R1 = self.tank.subsurface((48, 48), (48, 48))
        elif self.direction != utils.LEFT and d == utils.LEFT:
            self.tank_R0 = self.tank.subsurface((0, 96), (48, 48))
            self.tank_R1 = self.tank.subsurface((48, 96), (48, 48))
        elif self.direction != utils.RIGHT and d == utils.RIGHT:
            self.tank_R0 = self.tank.subsurface((0, 144), (48, 48))
            self.tank_R1 = self.tank.subsurface((48, 144), (48, 48))
        self.direction = d

    
    def is_ready_to_fire(self):
        current_time = pg.time.get_ticks()
        if current_time - self.last_fire_time >= utils.BULLET_COOL_DOWN:
            self.last_fire_time = current_time
            return True
        return False

    def fire(self):
        if self.is_ready_to_fire():
            bullet = Bullet(self.direction, self)
            group = self.groups()[0]
            group.add(bullet)
            self.fire_cool_down = False

    def update(self, keys):
        if keys[pg.K_LEFT]:
            self.set_direction_image(utils.LEFT)
            self.rect.x -= self.speed
            self.switch_image()
        if keys[pg.K_RIGHT]:
            self.set_direction_image(utils.RIGHT)
            self.rect.x += self.speed
            self.switch_image()
        if keys[pg.K_UP]:
            self.set_direction_image(utils.UP)
            self.rect.y -= self.speed
            self.switch_image()
        if keys[pg.K_DOWN]:
            self.set_direction_image(utils.DOWN)
            self.rect.y += self.speed
            self.switch_image()
        if keys[pg.K_SPACE]:
            self.fire()

        screen_rect = utils.get_screen_rect()
        self.rect.x = max(0, min(self.rect.x, screen_rect.width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, screen_rect.height - self.rect.height))