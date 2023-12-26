import pygame

#images in the background
class Things(pygame.sprite.Sprite):
    def __init__(self, x, y, image, index):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.index = index
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)


#images in the list
class ThingsInList(pygame.sprite.Sprite):
    def __init__(self, x, y, image, index):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.index = index
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
