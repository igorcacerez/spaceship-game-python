import pygame
from scripts.animatebg import AnimateBg
from scripts.scene import Scene
from scripts.text import Text
from scripts.settings import *

class Menu(Scene):

    def __init__(self):
        super().__init__()
        
        self.bg = AnimateBg("assets/menu/bg.png", [self.all_sprites])
        self.title = Text("assets/fonts/airstrike.ttf", 50, "SpaceShip Game", "white", [450, 300])
        self.text_info = Text("assets/fonts/airstrike.ttf", 21, "Precione Enter para jogar", "white", [508, 513])
       
    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.active = False  
        return super().events(event) 
        
    def update(self):
        self.bg.update()
        self.title.draw()
        self.text_info.drawFade()
        return super().update()

        
