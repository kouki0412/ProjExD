import pygame as pg
import random
import sys

class ScreenClass:
    def __init__(self,title,width_height,file):
        pg.display.set_caption("逃げろ！こうかとん")
        self.sfc = pg.display.set_mode(width_height)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(file)
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc,self.bgi_rct)


class BirdClass:

    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self,file,zoom,center):
        self.sfc = pg.image.load(file)
        self.sfc = pg.transform.rotozoom(self.sfc, 0,zoom)
        self.rct = self.sfc.get_rect()
        self.rct.center = center

    def blit(self,scrn_obj):
        scrn_obj.sfc.blit(self.sfc,self.rct)
    
    def update(self,scrn_obj):
        key_dct = pg.key.get_pressed()
        for key, delta in self.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]

            if check_bound(self.rct, scrn_obj.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]

class BombClass:

    def __init__(self,color,r,v,scrn_obj):
        self.sfc = pg.Surface((2*r, 2*r)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (r, r), r)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scrn_obj.rct.width)
        self.rct.centery = random.randint(0, scrn_obj.rct.height)
        self.vx = v[0]
        self.vy = v[1]
    
    def blit(self,scrn_obj):
        scrn_obj.sfc.blit(self.sfc,self.rct)
    
    def update(self,scrn_obj):
        self.rct.move_ip(self.vx,self.vy)
        tate, yoko = check_bound(self.rct,scrn_obj.rct)
        self.vx *= tate
        self.vy *= yoko
        self.blit(scrn_obj)

def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    clock =pg.time.Clock()
    # 練習１
    screen = ScreenClass("逃げろ！こうかとん",(1600,900),"fig/pg_bg.jpg")
    screen.blit()
    # 練習３
    tori = BirdClass("fig/3.png",2.0,(900, 400))
    # scrn_sfcにtori_rctに従って，tori_sfcを貼り付ける
    tori.blit(screen) 

    # 練習５
    bomb = BombClass((255,0,0),10,(1,1),screen)
    bomb.blit(screen)

    # 練習２
    while True:
        screen.blit() 

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        tori.update(screen)
        tori.blit(screen) # 練習3

        # 練習６
        bomb.update(screen)

        # 練習８
        if tori.rct.colliderect(bomb.rct):
            return

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()