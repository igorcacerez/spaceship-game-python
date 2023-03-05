import pygame
from scripts.obj import Obj
from scripts.settings import *

class AnimateBg: 
    def __init__(self, img, grup):
        self.bg = Obj(img, [0, -1], grup)
        self.bg2 = Obj(img, [0, HEIGHT], grup)
    
    def update(self):
        
        self.bg.rect.y += 1
        self.bg2.rect.y += 1
        
        if self.bg.rect.y >= HEIGHT:
            self.bg.rect.y = -HEIGHT
        
        if self.bg2.rect.y >= HEIGHT:
            self.bg2.rect.y = -HEIGHT