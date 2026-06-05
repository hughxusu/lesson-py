import pygame as pg

pg.init()
window = pg.display.set_mode((800, 600))
clock = pg.time.Clock()
is_running = True

while is_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

    clock.tick(60)
    pg.display.update()
    
pg.quit()