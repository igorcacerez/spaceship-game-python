import pygame
from scripts.elements.enemy import Enemy

class MediumShip(Enemy): 
    
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)
        
        self.speed = 3
        self.life = 3
        
    def update(self):
        self.animate(10, [
            "assets\/nave\/enemy2_0.png",
            "assets\/nave\/enemy2_1.png",
            "assets\/nave\/enemy2_2.png"
        ])
        return super().update()