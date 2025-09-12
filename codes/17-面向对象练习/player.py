import pygame as pg

tank_T1_0 = r"images/tank_T1_0.png"

class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        # 加载玩家坦克图片
        self.image = pg.image.load(tank_T1_0)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # 移动速度
        self.speed = 3
        
    def update(self, keys):
        """根据按键更新玩家位置"""
        if keys[pg.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pg.K_UP]:
            self.rect.y -= self.speed
        if keys[pg.K_DOWN]:
            self.rect.y += self.speed
            
        # 边界检查
        self.rect.x = max(0, min(self.rect.x, 720 - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, 720 - self.rect.height))