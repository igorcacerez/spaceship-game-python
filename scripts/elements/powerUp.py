import pygame
from scripts.elements.enemy import Enemy

class PowerUp(Enemy):
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)
        
        self.speed = 2
        
    def update(self):
        self.animate(16, [
            "assets\/nave\/powerup0.png",
            "assets\/nave\/powerup1.png",
            "assets\/nave\/powerup2.png"
        ])
        return super().update()