import pygame as pg
import sys
import random

def main():
    pg.display.set_caption("逃げろ!こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()

    bcsc_sfc = pg.image.load("fig/pg_bg.jpg")
    bcsc_rct = bcsc_sfc.get_rect()
    bcsc_rct.center = 800 , 450

    plyr_sfc = pg.image.load("fig/0.png")
    plyr_sfc = pg.transform.rotozoom(plyr_sfc,0,2.0)
    plyr_rct = plyr_sfc.get_rect()
    px, py = 900, 400
    plyr_rct.center = px,py

    bomb_sfc = pg.Surface((20,20))
    bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc,(255,0,0),(10,10),10)
    bomb_rct = bomb_sfc.get_rect()
    bx, by = (random.randint(0,scrn_rct.width),random.randint(0,scrn_rct.height))

    dx, dy = 1, 1

    clock = pg.time.Clock()
    #clock.tick(0.5)
    while True:
        scrn_sfc.blit(bcsc_sfc,bcsc_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        key_list = pg.key.get_pressed()
        if key_list[pg.K_UP]:
            py -= 1
        if key_list[pg.K_DOWN]:
            py += 1
        if key_list[pg.K_LEFT]:
            px -= 1
        if key_list[pg.K_RIGHT]:
            px += 1
        plyr_rct.center = px,py
        
        bx += dx
        by += dy
        if bx < 0 or scrn_rct.width < bx:
            dx *= -1
        if by < 0 or scrn_rct.height < by:
            dy *= -1
        bomb_rct.center = bx, by
        if plyr_rct.colliderect(bomb_rct):
            clock.tick(0.5)
            return
        scrn_sfc.blit(plyr_sfc,plyr_rct)
        scrn_sfc.blit(bomb_sfc,bomb_rct)
        pg.display.update()
        clock.tick(1000)
        

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()