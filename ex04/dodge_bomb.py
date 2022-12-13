import pygame as pg
import sys
import random

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


def move_bomb1(scrn_rct,bomb_rct):
    global dx,dy
    if bomb_rct.left < scrn_rct.left or bomb_rct.right > scrn_rct.right:
        dx *= -1
    if bomb_rct.top < scrn_rct.top or bomb_rct.bottom > scrn_rct.bottom:
        dy *= -1
    bomb_rct.centerx += dx
    bomb_rct.centery += dy

def move_bomb2(scrn_rct,bomb_rct,plyr_rct):
    px,py= plyr_rct.center
    bx,by= bomb_rct.center
    if px < bx:
        Dx = -1
    else:
        Dx = 1

    if py < by:
        Dy = -1
    else:
        Dy = 1
    
    if bomb_rct.left < scrn_rct.left or bomb_rct.right > scrn_rct.right:
        Dx *= -1
    if bomb_rct.top < scrn_rct.top or bomb_rct.bottom > scrn_rct.bottom:
        Dy *= -1
    
    if random.randint(0,1)==0:
        bomb_rct.centerx += Dx
    else:
        bomb_rct.centery += Dy

def main():
    global mode

    pg.display.set_caption("逃げろ!こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()

    bcsc_sfc = pg.image.load("fig/pg_bg.jpg")
    bcsc_rct = bcsc_sfc.get_rect()
    bcsc_rct.center = 800 , 450

    plyr_sfc = pg.image.load("fig/3.png")
    plyr_sfc = pg.transform.rotozoom(plyr_sfc,0,2.0)
    plyr_rct = plyr_sfc.get_rect()
    plyr_rct.center = 900, 400

    bomb_sfc = pg.Surface((20,20))
    bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc,(255,0,0),(10,10),10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.center = (random.randint(0,scrn_rct.width),random.randint(0,scrn_rct.height))

    clock = pg.time.Clock()

    #clock.tick(0.5)
    while True:
        scrn_sfc.blit(bcsc_sfc,bcsc_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        key_list = pg.key.get_pressed()

        move_player(scrn_rct,plyr_rct,key_list)

        if key_list[pg.K_1]:
            mode = 1
        elif key_list[pg.K_2]:
            mode = 2
        if mode == 1:
            move_bomb1(scrn_rct,bomb_rct)
        else:
            move_bomb2(scrn_rct,bomb_rct,plyr_rct)    

        if plyr_rct.colliderect(bomb_rct):
            gameover_sfc = pg.image.load("fig/8.png")
            gameover_sfc = pg.transform.rotozoom(gameover_sfc,0,2.0)
            gameover_rct = gameover_sfc.get_rect()
            px, py = plyr_rct.center
            gameover_rct.center = px,py

            fonto = pg.font.Font(None,160)
            txt = fonto.render("GAME OVER!",True, (255,120,255))
            
            scrn_sfc.blit(bomb_sfc,bomb_rct)
            scrn_sfc.blit(gameover_sfc,gameover_rct)
            scrn_sfc.blit(txt,(450,400))
            pg.display.update()
            clock.tick(0.5)
            return
        scrn_sfc.blit(plyr_sfc,plyr_rct)
        scrn_sfc.blit(bomb_sfc,bomb_rct)
        pg.display.update()
        clock.tick(1000)
        

if __name__ == "__main__":
    pg.init()
    dx, dy = 1, 1
    mode = 1
    main()
    pg.quit()
    sys.exit()