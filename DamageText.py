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

