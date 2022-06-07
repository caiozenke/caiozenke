import pygame as py
from config import *


class Blocos(py.sprite.Sprite):
    def __init__(self,pos,grupos):
        super().__init__(grupos)
        self.image = py.Surface ((blocos_tam, blocos_tam))
        self.image.fill(blocos_cor)
        self.rect = self.image.get_rect(topleft =pos)