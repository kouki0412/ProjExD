import random
import sys

import pygame as pg
import time

MAX_BOMB = 10

bomb_time = None


class ScreenClass:
    def __init__(self,title,width_height,file):
        pg.display.set_caption("負けるな！こうかとん")
        self.sfc = pg.display.set_mode(width_height)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(file)
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc,self.bgi_rct)

class BirdClass(pg.sprite.Sprite):

    key_delta = {
        pg.K_UP:    [0, -1, 0],
        pg.K_DOWN:  [0, +1, 1],
        pg.K_LEFT:  [-1, 0, 2],
        pg.K_RIGHT: [+1, 0, 3],
    }

    def __init__(self,file,zoom,center):
        #pg.sprite.Sprite.__init__(self,self.container)
        self.sfc = pg.image.load(file)
        self.sfc = pg.transform.rotozoom(self.sfc, 0,zoom)
        self.rct = self.sfc.get_rect()
        self.rct.center = center
        self.dic = 1

        #self.image = self.sfc
        #self.rect = self.rct
        
    def blit(self,scrn_obj):
        scrn_obj.sfc.blit(self.sfc,self.rct)
    
    def update(self,scrn_obj):
        key_dct = pg.key.get_pressed()
        for key, delta in self.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                self.dic = delta[2]

            if check_bound(self.rct, scrn_obj.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        
        self.blit(scrn_obj)
#ビームを管理するクラス
class BeamClass:
    def __init__(self,color,v,bird_obj,scrn_obj):
        self.sfc = pg.Surface((40, 40))
        self.sfc.set_colorkey((0,0,0))
        pg.draw.circle(self.sfc, color, (20, 20), 20)
        self.rct = self.sfc.get_rect()
        self.rct.center = bird_obj.rct.center
        self.vx = v[0]
        self.vy = v[1]

    def blit(self,scrn_obj):
        scrn_obj.sfc.blit(self.sfc,self.rct)

    def update(self,scrn_obj,bombs):
        self.rct.move_ip(self.vx,self.vy)

        tate, yoko = check_bound(self.rct,scrn_obj.rct)
        self.vx *= tate
        self.vy *= yoko

        del_list = []

        for i in range(len(bombs)):
            if self.rct.colliderect(bombs[i].rct):
                del_list.append(i)

        #index指定なのでout_of_rangeを防ぐために一旦別のリストに入れる
        for i in del_list:
            kill_bomb(bombs,i)

        self.blit(scrn_obj)


class BombClass(pg.sprite.Sprite):

    def __init__(self,color,r,v,scrn_obj):
        self.sfc = pg.Surface((2*r, 2*r))
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

#テキストを管理するクラス
class TextClass:
    def __init__(self,font,size,txt,color,pos):
        self.font = pg.font.Font(font,size)
        self.text = self.font.render(txt,True,color)
        self.pos = pos
    
    def blit(self,scrn_obj):
        scrn_obj.sfc.blit(self.text,self.pos)

def make_bomb(bombs,scrn_obj):
    global bomb_time
    now_time = time.time()
    if len(bombs)<MAX_BOMB and now_time-bomb_time>1:
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        v = (random.choice([-1,1]),random.choice([-1,1]))
        bomb = BombClass((255,0,0),10,v,scrn_obj)
        bomb.blit(scrn_obj)
        bombs.append(bomb)
        bomb_time = now_time

#指定がなければ一番後ろを消す
def kill_bomb(bombs,index=-1):
    global bomb_time
    now_time = time.time()
    if len(bombs)>0 and now_time-bomb_time>1:
        del bombs[index]
        bomb_time = now_time

def check_bound(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    global bomb_time

    clock =pg.time.Clock()
    bomb_time = -1
    screen = ScreenClass("逃げろ！こうかとん",(1600,900),"fig/pg_bg.jpg")
    screen.blit()

    sound_file = "ex05/mydata/BGM.mp3"
    pg.mixer.init(frequency = 44100)
    pg.mixer.music.load(sound_file)
    pg.mixer.music.set_volume(0.5)
    pg.mixer.music.play(-1)    
    
    tori = BirdClass("fig/3.png",2.0,(900, 400))
    tori.blit(screen) 

    bombs = []
    make_bomb(bombs,screen)

    beam = None

    spe_tech_time = time.time()

    while True:
        screen.blit() 

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key_dct = pg.key.get_pressed()
        tori.update(screen)

        
        if key_dct[pg.K_0]:
            make_bomb(bombs,screen)
        if key_dct[pg.K_1]:
            kill_bomb(bombs)
        if key_dct[pg.K_SPACE]:
            v = (random.choice(range(-2,3)),random.choice(range(-2,3)))
            beam = BeamClass((0,0,255),(v),tori,screen)
            beam_time = time.time()


        if beam != None:
            beam.update(screen,bombs)
            if time.time()-beam_time > 2:
                beam = None            

        gameover = False
        for bomb in bombs:
            bomb.update(screen)
            if tori.rct.colliderect(bomb.rct):
                gameover = True
        else:
            if gameover:
                center = tori.rct.center
                sad_tori = BirdClass("fig/8.png",2.0,center)
                sad_tori.blit(screen) 

                gameover = TextClass(None,160,"GAME OVER!",(255,120,255),(450,400))
                gameover.blit(screen)

                pg.display.update()
                clock.tick(0.5)
                return
                
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()