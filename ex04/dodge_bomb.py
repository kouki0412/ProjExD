import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ!こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))

    bcsc_sfc = pg.image.load("fig/pg_bg.jpg")
    bcsc_rct = bcsc_sfc.get_rect()
    bcsc_rct.center = 800 , 450
    clock = pg.time.Clock()
    #clock.tick(0.5)
    while True:
        scrn_sfc.blit(bcsc_sfc,bcsc_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        pg.display.update()
        clock.tick(1000)
        
    


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()