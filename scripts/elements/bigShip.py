import pygame
from scripts.elements.enemy import Enemy

class BigShip(Enemy): 
    
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)
        
        self.life = 6
        
    def update(self):
        self.animate(10, [
            "assets\/nave\/enemy3_0.png",
            "assets\/nave\/enemy3_1.png",
            "assets\/nave\/enemy3_2.png"
        ])
        return super().update()