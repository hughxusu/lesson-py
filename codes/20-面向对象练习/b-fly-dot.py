import pygame as pg

# 定义小圆点精灵类
class MovingDot(pg.sprite.Sprite):
    def __init__(self, x, y, radius, speed, color):
        super().__init__()
        # 创建一个透明Surface，大小为圆点的直径
        self.image = pg.Surface((radius * 2, radius * 2), pg.SRCALPHA)
        # 在Surface上绘制圆点
        pg.draw.circle(self.image, color, (radius, radius), radius)
        # 设置精灵的位置矩形
        self.rect = self.image.get_rect(center=(x, y))
        # 存储移动速度
        self.speed = speed
        # 存储窗口宽度，用于边界检测
        self.window_width = 800
    
    def update(self):
        # 更新圆点位置（向右移动）
        self.rect.x += self.speed
        # 当圆点到达右边界时，回到左边重新开始
        if self.rect.right > self.window_width:
            self.rect.left = 0

            
pg.init()
window = pg.display.set_mode((800, 600))
clock = pg.time.Clock()
is_running = True

# 创建精灵组
all_sprites = pg.sprite.Group()

# 创建小圆点精灵实例并添加到精灵组
dot = MovingDot(x=0, y=300, radius=10, speed=3, color=(255, 0, 0))
all_sprites.add(dot)

while is_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

    # 更新所有精灵
    all_sprites.update()

    # 清空窗口（填充黑色背景）
    window.fill((255, 255, 255))
    
    # 绘制所有精灵
    all_sprites.draw(window)

    clock.tick(60)
    pg.display.update()
    
pg.quit()