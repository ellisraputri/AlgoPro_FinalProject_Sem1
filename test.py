from img_text_display import Displaying
import pygame
dis = Displaying()

pygame.init()
#display
displays = Displaying()
screen = pygame.display.set_mode((displays.screen_width, displays.screen_height))

#the game title
pygame.display.set_caption('Game')

run = True
while run:
    screen.blit(dis.images.restart_img, (200,200))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()

