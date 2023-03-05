import json
import random
import pygame
from scripts.animatebg import AnimateBg
from scripts.elements.bigShip import BigShip
from scripts.elements.mediumShip import MediumShip
from scripts.elements.powerUp import PowerUp
from scripts.elements.smallShip import SmallShip
from scripts.elements.spaceship import SpaceShip
from scripts.explosion import Explosion
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *
from scripts.text import Text

class Game(Scene):

    def __init__(self):
        super().__init__()

        aux = json.load(open("assets/score.json"))
        self.record = aux["record"]

        self.bg = AnimateBg("assets/menu/bg.png", [self.all_sprites])
        self.spaceship = SpaceShip("assets/nave/nave1.png", [600, 600], [self.all_sprites])
        
        self.enemy_group = pygame.sprite.Group()
        self.tick = 0
        
        self.life1 = Obj("assets/hud/nave.png", [30, 60], [self.all_sprites])
        self.life2 = Obj("assets/hud/nave.png", [70, 60], [self.all_sprites])
        self.life3 = Obj("assets/hud/nave.png", [110, 60], [self.all_sprites])
        
        self.power_group = pygame.sprite.Group()
        
        self.pontos = 0
        self.text_pontos = Text("assets/fonts/airstrike.ttf", 25, "Pontos: ", "white", [30, 30])
        self.text_pontos_num = Text("assets/fonts/airstrike.ttf", 25, str(self.pontos), "white", [150, 30])
        
        self.text_record = Text("assets/fonts/airstrike.ttf", 25, "Record: ", "white", [WIDTH - 220, 30])
        self.text_record_num = Text("assets/fonts/airstrike.ttf", 25, str(self.record), "white", [WIDTH - 100, 30])
        
        self.music = pygame.mixer.Sound("assets/sounds/bg.ogg")
        self.music.play(-1)
        
    def spaw_enemy(self):
        self.tick += 1
        
        if self.tick == 60:
            BigShip("assets/nave/enemy3_0.png", [random.randint(100, WIDTH - 200), -100], [self.all_sprites, self.enemy_group])
        elif self.tick == 180:
            MediumShip("assets/nave/enemy2_0.png", [random.randint(100, WIDTH - 200), -100], [self.all_sprites, self.enemy_group])
            MediumShip("assets/nave/enemy2_0.png", [random.randint(100, WIDTH - 200), -100], [self.all_sprites, self.enemy_group])
        elif self.tick == 280:
            SmallShip("assets/nave/enemy0.png", [random.randint(100, WIDTH - 200), -100], [self.all_sprites, self.enemy_group])
            SmallShip("assets/nave/enemy0.png", [random.randint(100, WIDTH - 200), -100], [self.all_sprites, self.enemy_group])
            SmallShip("assets/nave/enemy0.png", [random.randint(100, WIDTH - 200), -100], [self.all_sprites, self.enemy_group])
            SmallShip("assets/nave/enemy0.png", [random.randint(100, WIDTH - 200), -100], [self.all_sprites, self.enemy_group])
            PowerUp("assets/nave/powerup0.png", [random.randint(100, WIDTH - 200), -100], [self.all_sprites, self.power_group])
            self.tick = 0
            
    def hub(self):
        if self.spaceship.life == 2:
            self.life3.kill()
        elif self.spaceship.life == 1:
            self.life2.kill()
        elif self.spaceship.life == 0:
            self.life1.kill()
        else: 
            if self.life1 not in self.all_sprites:
                self.all_sprites.add(self.life1)
            if self.life2 not in self.all_sprites:
                self.all_sprites.add(self.life2)
            if self.life3 not in self.all_sprites:
                self.all_sprites.add(self.life3)
                 
    def colision(self):
        for shot in self.spaceship.shots:
            for enemy in self.enemy_group:
                if shot.rect.colliderect(enemy.rect):
                    shot.kill()
                    enemy.life -= 1
                    self.pontos += 1
                    self.text_pontos_num.update_text(str(self.pontos))
                    
                    sound = pygame.mixer.Sound("assets/sounds/block.ogg")
                    sound.play()
                    
                    if enemy.life <= 0:
                        x = enemy.rect.x + enemy.rect.width / 2
                        y = enemy.rect.y + enemy.rect.height / 2
                        Explosion("assets/explosion/0.png", [x, y], [self.all_sprites])
                    
        for enemy in self.enemy_group:
            if enemy.rect.colliderect(self.spaceship.rect):
                enemy.kill()
                self.spaceship.life -= 1
                self.spaceship.level = 1
                sound = pygame.mixer.Sound("assets/sounds/damage.ogg")
                sound.play()
                
        for power in self.power_group:
            if power.rect.colliderect(self.spaceship.rect):
                power.kill()
                self.spaceship.level += 1
                sound = pygame.mixer.Sound("assets/sounds/levelup.ogg")
                sound.play()
                self.pontos += 10
                if self.spaceship.level > 7 and self.spaceship.life < 3:
                    self.spaceship.life += 1
    
    def game_over(self):
        if self.spaceship.life <= 0:
            if self.pontos > self.record:
                aux = {"record": self.pontos}
                json.dump(aux, open("assets/score.json", "w"))
            self.music.stop()
            self.active = False
        
    def update(self):
        self.spaceship.shots.draw(self.display)
        self.spaceship.shots.update()
        self.colision()
        self.bg.update()
        self.spaceship.update()
        self.spaw_enemy()
        self.text_pontos.draw()
        self.text_pontos_num.draw()
        self.text_record.draw()
        self.text_record_num.draw()
        self.game_over()
        self.hub()
        return super().update()