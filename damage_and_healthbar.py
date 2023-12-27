import pygame

class DamageText(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, colour):
        pygame.sprite.Sprite.__init__(self)
        font =pygame.font.Font('Assets/font/Pixeltype.ttf',40)
        self.image = font.render(damage, True, colour)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.counter=0

    def update(self):
        #move damage text up
        self.rect.y -= 1
        #delete text after few seconds
        self.counter +=1
        if self.counter > 30:
            self.kill()
    
    
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

