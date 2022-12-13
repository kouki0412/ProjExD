import pygame as pg
import sys
import random

def mode_change():
    pass


def check_bomb_board(scrn_rct,bomb_rct):
    global dx,dy
    if bomb_rct.left < scrn_rct.left or bomb_rct.right > scrn_rct.right:
        dx *= -1
    if bomb_rct.top < scrn_rct.top or bomb_rct.bottom > scrn_rct.bottom:
        dy *= -1
    bomb_rct.centerx += dx
    bomb_rct.centery += dy

KEYS = [pg.K_UP,pg.K_DOWN,pg.K_LEFT,pg.K_RIGHT]
DXY = {pg.K_UP:(0,-1),pg.K_DOWN:(0,1),pg.K_LEFT:(-1,0),pg.K_RIGHT:(1,0)}

def move_player(scrn_rct,plyr_rct,key_list):
    for key in KEYS:
        if key_list[key]:
            Dx, Dy = DXY[key]
            plyr_rct.centerx += Dx
            plyr_rct.centery += Dy

            if plyr_rct.left < scrn_rct.left or plyr_rct.right > scrn_rct.right:
                plyr_rct.centerx -= Dx
            if plyr_rct.top < scrn_rct.top or plyr_rct.bottom > scrn_rct.bottom:
                plyr_rct.centery -= Dy

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
    clock = pg.time.Clock()

    #clock.tick(0.5)
    while True:
        scrn_sfc.blit(bcsc_sfc,bcsc_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        key_list = pg.key.get_pressed()

        move_player(scrn_rct,plyr_rct,key_list)

        check_bomb_board(scrn_rct,bomb_rct)

        if plyr_rct.colliderect(bomb_rct):
            clock.tick(0.5)
            return
        scrn_sfc.blit(plyr_sfc,plyr_rct)
        scrn_sfc.blit(bomb_sfc,bomb_rct)
        pg.display.update()
        clock.tick(1000)
        

if __name__ == "__main__":
    pg.init()
    dx, dy = 1, 1
    main()
    pg.quit()
    sys.exit()