import pygame as pg
import sys
import random

def main():
    pg.display.set_caption("逃げろ!こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))

    bcsc_sfc = pg.image.load("fig/pg_bg.jpg")
    bcsc_rct = bcsc_sfc.get_rect()
    bcsc_rct.center = 800 , 450

    plyr_sfc = pg.image.load("fig/0.png")
    plyr_sfc = pg.transform.rotozoom(plyr_sfc,0,2.0)
    plyr_rct = plyr_sfc.get_rect()
    px, py = 900, 400
    plyr_rct.center = px,py

    bomb_sfc = pg.Surface((100,100))
    bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc,(255,0,0),(50,50),10)
    bx, by = (random.randint(0,1600),random.randint(0,900))
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
        scrn_sfc.blit(plyr_sfc,plyr_rct)
        scrn_sfc.blit(bomb_sfc,(bx,by))
        pg.display.update()
        clock.tick(1000)
        
    


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()