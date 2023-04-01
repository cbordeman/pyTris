from settings import *
import sys
import pygame

class App:
    def __init__(self):
        pg.display.set_caption("PyTris!")
        self.screen = pg.display.set_mode(FIELD_RES)
        self.clock = pg.time.Clock()

    def update(self):
        self.clock.tick(FPS)