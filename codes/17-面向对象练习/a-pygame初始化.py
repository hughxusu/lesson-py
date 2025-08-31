import pygame as pg

pg.init()

window = pg.display.set_mode((800, 600))
print(window)
pg.display.set_caption("maze")

clock = pg.time.Clock()

window.fill((227, 227, 227))
pg.draw.line(window, 'red', (50, 50), (150, 150), 5) # 绘制线
pg.draw.rect(window, 'green', (200, 200, 100, 100)) # 绘制矩形
pg.draw.circle(window, 'blue', (400, 300), 50) # 绘制圆
pg.draw.polygon(window, 'yellow', ((500, 50), (600, 150), (700, 50))) # 绘制多边形
pg.draw.ellipse(window, 'purple', (300, 400, 200, 100)) # 绘制椭圆
pg.draw.arc(window, 'orange', (100, 100, 200, 100), 0, 3.14, 5) # 绘制弧线

pg.key.set_repeat(100, 100) # 按键重复
hugging_face = pg.image.load('hugging_face.png')
hugging_face = pg.transform.scale(hugging_face, (200, 200))
window.blit(hugging_face, (0, 0))
pg.display.update()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            print('mouse button pressed')

        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            print('space key pressed')  

    

    clock.tick(60)

    

