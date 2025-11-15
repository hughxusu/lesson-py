import pygame as pg
import utils

BULLET_IMG_UP = r"images/bullet_up.png"
BULLET_IMG_DOWN = r"images/bullet_down.png"
BULLET_IMG_LEFT = r"images/bullet_left.png"
BULLET_IMG_RIGHT = r"images/bullet_right.png"

class Bullet(pg.sprite.Sprite):
    def __init__(self, direction, owner):
        super().__init__()
        self.direction = direction
        if self.direction == utils.UP:
            self.image = pg.image.load(BULLET_IMG_UP).convert_alpha()
        elif self.direction == utils.DOWN:
            self.image = pg.image.load(BULLET_IMG_DOWN).convert_alpha()
        elif self.direction == utils.LEFT:
            self.image = pg.image.load(BULLET_IMG_LEFT).convert_alpha()
        elif self.direction == utils.RIGHT:
            self.image = pg.image.load(BULLET_IMG_RIGHT).convert_alpha()
        self.speed = 5

        self.rect = self.image.get_rect()
        self.rect.center = owner.rect.center
        
    def update(self, keys):
        if self.direction == utils.UP:
            self.rect.y -= self.speed
        elif self.direction == utils.DOWN:
            self.rect.y += self.speed
        elif self.direction == utils.LEFT:
            self.rect.x -= self.speed
        elif self.direction == utils.RIGHT:
            self.rect.x += self.speed
        
        screen_rect = utils.get_screen_rect()
        if not self.rect.colliderect(screen_rect):
            self.kill()