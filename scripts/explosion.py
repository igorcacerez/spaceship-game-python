import pygame
from scripts.obj import Obj

class Explosion(Obj):
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)
        
        self.ticks = 0
        
    def update(self):
        self.animate(5, [
            "assets\/explosion\/0.png",
            "assets\/explosion\/1.png",
            "assets\/explosion\/2.png",
            "assets\/explosion\/3.png",
            "assets\/explosion\/4.png",
        ])
        
        self.ticks += 1
        if self.ticks > 25:
            self.kill()
        
        return super().update()