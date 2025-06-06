import pygame
from scripts.animatebg import AnimateBg
from scripts.scene import Scene
from scripts.settings import HEIGHT
from scripts.text import Text


class GameOver(Scene):

    def __init__(self):
        super().__init__()
        
        self.bg = AnimateBg("assets/menu/bg.png", [self.all_sprites])
        self.title = Text("assets/fonts/airstrike.ttf", 50, "GAME OVER", "white", [501, 350])
       
    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.active = False  
        return super().events(event) 
        
    def update(self):
        self.bg.update()
        self.title.draw()
        return super().update()
