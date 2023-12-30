import pygame

class Button():
    def __init__(self, surface,x,y,image,size_x,size_y, hint=False):
        self.image = pygame.transform.scale(image, (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.clicked = False
        self.surface = surface
        self.click_sound = pygame.mixer.Sound('Assets/audio/sfx/click.wav')
        self.hint = hint
    
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
                if self.hint == False:
                    self.click_sound.play()

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked=False
        
        self.surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

    
    
            