import pygame
from scripts.obj import Obj

class Shot(Obj):
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)
        
        self.speed = 5
        
    def update(self):
        self.rect.y -= self.speed
        
        if self.rect.y < -100:
            self.kill()