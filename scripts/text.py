import pygame

class Text:
    
    def __init__(self, font, size, text, color, pos, speed = 5):
        
        self.display = pygame.display.get_surface()
        self.font = pygame.font.Font(font, size)
        self.text = self.font.render(text, True, color).convert_alpha()
        self.position = pos
        self.alpha = 255
        self.speed = speed
        self.color = color
        
    def draw(self):
        self.display.blit(self.text, self.position)
        
    def update_text(self, text):
        self.text = self.font.render(text, True, self.color).convert_alpha()
        
    def drawFade(self):
        
        if self.alpha > 0:
            self.alpha -= self.speed
        else: 
            self.alpha = 255
        
        self.text.set_alpha(self.alpha)
        self.display.blit(self.text, self.position)