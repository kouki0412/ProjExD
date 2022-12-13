import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ!こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))

    bcsc_sfc = pg.image.load("fig/pg_bg.jpg")
    bcsc_rct = bcsc_sfc.get_rect()
    bcsc_rct.center = 0 , 0
    clock = pg.time.Clock()
    clock.tick(0.5)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()