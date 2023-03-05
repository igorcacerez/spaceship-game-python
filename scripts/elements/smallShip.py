import pygame
from scripts.elements.enemy import Enemy

class SmallShip(Enemy): 
    
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)
        
        self.speed = 6
        self.life = 1
        
    def update(self):
        self.animate(10, [
            "assets\/nave\/enemy0.png",
            "assets\/nave\/enemy1.png",
            "assets\/nave\/enemy2.png"
        ])
        return super().update()