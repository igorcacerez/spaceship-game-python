import pygame
from scripts.elements.shot import Shot
from scripts.obj import Obj
from scripts.settings import *

class SpaceShip(Obj):
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)
        
        self.direction = pygame.math.Vector2()
        self.speed = 1
        self.life = 3
        self.level = 1
        self.shots = pygame.sprite.Group()
        self.ticks_shot = 0

    def input(self): 
        key = pygame.key.get_pressed()
        
        if (key[pygame.K_w] or key[pygame.K_UP]):
            self.direction.y -= 1
        elif (key[pygame.K_s] or key[pygame.K_DOWN]):
            self.direction.y += 1
        else: 
            self.direction.y = 0
            
        
        if (key[pygame.K_a] or key[pygame.K_LEFT]):
            self.direction.x -= 1
        elif (key[pygame.K_d] or key[pygame.K_RIGHT]):
            self.direction.x += 1
        else:
            self.direction.x = 0
            
        if key[pygame.K_SPACE]:
            self.ticks_shot += 1
            if self.ticks_shot > 30: 
                self.ticks_shot = 0
                sound = pygame.mixer.Sound("assets/sounds/shot.ogg")
                sound.play()
                if self.level == 1: 
                    Shot("assets/tiros/tiro1.png", [self.rect.x + 30, self.rect.y - 20], [self.shots])
                elif self.level == 2:
                    Shot("assets/tiros/tiro2.png", [self.rect.x + 30, self.rect.y - 20], [self.shots])
                elif self.level == 3:
                    Shot("assets/tiros/tiro3.png", [self.rect.x + 30, self.rect.y - 20], [self.shots])
                elif self.level == 4: 
                    Shot("assets/tiros/tiro1.png", [self.rect.x, self.rect.y - 20], [self.shots])
                    Shot("assets/tiros/tiro1.png", [self.rect.x + 60, self.rect.y - 20], [self.shots])
                elif self.level == 5: 
                    Shot("assets/tiros/tiro2.png", [self.rect.x, self.rect.y - 20], [self.shots])
                    Shot("assets/tiros/tiro2.png", [self.rect.x + 60, self.rect.y - 20], [self.shots])
                elif self.level == 6: 
                    Shot("assets/tiros/tiro3.png", [self.rect.x, self.rect.y - 20], [self.shots])
                    Shot("assets/tiros/tiro3.png", [self.rect.x + 60, self.rect.y - 20], [self.shots])
                else: 
                    Shot("assets/tiros/tiro2.png", [self.rect.x, self.rect.y - 20], [self.shots])
                    Shot("assets/tiros/tiro2.png", [self.rect.x + 20, self.rect.y - 20], [self.shots])
                    Shot("assets/tiros/tiro2.png", [self.rect.x + 40, self.rect.y - 20], [self.shots])
                    Shot("assets/tiros/tiro2.png", [self.rect.x + 60, self.rect.y - 20], [self.shots])
            
    def limit(self):
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > WIDTH - self.rect.width:
            self.rect.x = WIDTH - self.rect.width
            
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > HEIGHT - self.rect.height:
            self.rect.y = HEIGHT - self.rect.height     
            
    def move(self):
        self.rect.center += self.direction * self.speed
        
    def update(self):
        self.animate(10, ["assets\/nave\/nave0.png","assets\/nave\/nave1.png","assets\/nave\/nave2.png"])
        self.input()
        self.limit()
        self.move()