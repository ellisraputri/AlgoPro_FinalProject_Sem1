import pygame

class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x 
        self.y = y
        self.hp = hp
        self.max_hp = max_hp
    
    def draw (self, hp, surf):
        #update hp as game progress
        self.hp = hp
        #calculate health ratio
        ratio = self.hp / self.max_hp

        pygame.draw.rect(surf, (255,0,0), (self.x, self.y, 150, 20))
        pygame.draw.rect(surf, (0,255,0), (self.x, self.y, 150*ratio, 20))