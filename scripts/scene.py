import pygame
from scripts.fade import Fade
from scripts.obj import Obj

class Scene:

    def __init__(self):
        
        self.display = pygame.display.get_surface()
        self.all_sprites = pygame.sprite.Group()
        self.active = True
        self.fade = Fade()

    def events(self, event):
        pass

    def draw(self):
        self.all_sprites.draw(self.display)

    def update(self):
        self.fade.draw()
        self.all_sprites.update()

