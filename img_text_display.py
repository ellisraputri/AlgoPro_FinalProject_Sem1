import pygame
from transition import Transition

class Displaying():
    def __init__(self):
        #screen width and height
        self.bottom_panel = 150
        self.screen_width = 1000
        self.screen_height = 500 + self.bottom_panel

        #images
        self.bg_main = pygame.image.load("Assets/images/background/main_menu.png").convert_alpha()
        self.bg_main = pygame.transform.scale(self.bg_main, (self.bg_main.get_width()*1.25, self.bg_main.get_height()*1.25))

        self.main_logo = pygame.image.load("Assets/images/icon/main_menu_logo.png").convert_alpha()
        self.main_logo = pygame.transform.scale(self.main_logo, (self.main_logo.get_width()*0.5, self.main_logo.get_height()*0.5))

        self.bg_image = pygame.image.load("Assets/images/background/background.png").convert_alpha()
        self.bg_image = pygame.transform.scale(self.bg_image, (self.bg_image.get_width()*1.25, self.bg_image.get_height()*1.25))

        self.panel_image = pygame.image.load("Assets/images/icon/panel.png").convert_alpha()
        self.panel_image = pygame.transform.scale(self.panel_image, (self.panel_image.get_width()*1.25, self.panel_image.get_height()))

        self.sword_image = pygame.image.load("Assets/images/icon/sword.png").convert_alpha()
        self.potion_img = pygame.image.load("Assets/images/icon/potion.png").convert_alpha()
        self.victory_img = pygame.image.load("Assets/images/icon/victory.png").convert_alpha()
        self.defeat_img = pygame.image.load("Assets/images/icon/defeat.png").convert_alpha()
        self.restart_img = pygame.image.load("Assets/images/icon/restart.png").convert_alpha()
        self.next_stage_img = pygame.image.load("Assets/images/icon/next_stage.png").convert_alpha()

        self.new_game_img = pygame.image.load("Assets/images/icon/button_main_1.png").convert_alpha()
        self.new_game_img = pygame.transform.scale(self.new_game_img, (self.new_game_img.get_width()*0.45, self.new_game_img.get_height()*0.45))

        self.continue_game_img = pygame.image.load("Assets/images/icon/button_main_2.png").convert_alpha()
        self.continue_game_img = pygame.transform.scale(self.continue_game_img, (self.continue_game_img.get_width()*0.45, self.continue_game_img.get_height()*0.45))

        self.exit_img = pygame.image.load("Assets/images/icon/button_main_3.png").convert_alpha()
        self.exit_img = pygame.transform.scale(self.exit_img, (self.exit_img.get_width()*0.45, self.exit_img.get_height()*0.45))

        self.scene1_bg = pygame.image.load("Assets/images/background/scene_1.png").convert_alpha()
        self.scene1_bg = pygame.transform.scale(self.scene1_bg, (self.scene1_bg.get_width()*1.5, self.scene1_bg.get_height()*1.5))

        self.boy_icon = pygame.image.load("Assets/images/icon/boy_icon.png").convert_alpha()
        self.boy_icon = pygame.transform.scale(self.boy_icon, (self.boy_icon.get_width()*5.5, self.boy_icon.get_height()*5.5))
        
        self.vampire_icon = pygame.image.load("Assets/images/icon/vampire_icon.png").convert_alpha()
        self.vampire_icon = pygame.transform.scale(self.vampire_icon, (self.vampire_icon.get_width()*3.5, self.vampire_icon.get_height()*3.5))

        self.boy_text_icon = pygame.image.load("Assets/images/icon/boy_text_icon.png").convert_alpha()
        self.boy_text_icon = pygame.transform.scale(self.boy_text_icon, (self.boy_text_icon.get_width()*0.35, self.boy_text_icon.get_height()*0.35))

        self.vampire_text_icon = pygame.image.load("Assets/images/icon/vampire_text_icon.png").convert_alpha()
        self.vampire_text_icon = pygame.transform.scale(self.vampire_text_icon, (self.vampire_text_icon.get_width()*0.35, self.vampire_text_icon.get_height()*0.35))

        self.skip_button = pygame.image.load("Assets/images/icon/skip_button.png").convert_alpha()

        self.fight1 = pygame.image.load("Assets/images/icon/fight1.png").convert_alpha()
        self.fight1 = pygame.transform.scale(self.fight1, (self.fight1.get_width()*0.35, self.fight1.get_height()*0.35))

        #text
        self.font =pygame.font.Font('Assets/font/Pixeltype.ttf',40)

    #draw functions
    def draw_bg(self,screen,background):
        screen.blit(background,(0,0))

    def draw_panel(self,screen, screen_height, bottom_panel, knight, enemy_list):
        #draw panel rectangle
        screen.blit(self.panel_image, (0, screen_height - bottom_panel))
        #show knight stats
        self.draw_text(f'{knight.name} HP: {knight.hp}', self.font, (255,0,0), 135, screen_height-bottom_panel+25, screen, 40)
        #show bandit stats
        for count, i in enumerate(enemy_list):
            self.draw_text(f'Black Wolf {count+1} HP: {i.hp}', self.font, (255,0,0), 660, screen_height-bottom_panel+25 + count*60, screen, 40)

    def draw_text (self, text, font, text_col, x, y, screen, size):
        self.font =pygame.font.Font('Assets/font/Pixeltype.ttf',size)
        img = font.render(text, True, text_col)
        img_rect= img.get_rect(center = (x,y))
        screen.blit(img, img_rect)

    def draw_sword (self, screen, pos):
        screen.blit(self.sword_image, pos)

    def draw_buttons(self, screen, image, x, y):
        image_rect = image.get_rect(center=(x,y))
        screen.blit(image, image_rect)


class FadeTransition():
    def __init__(self, next_state, screen_width, screen_height):
        self.next_state = next_state
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.transition = Transition(self.next_state, self.screen_width, self.screen_height)
    def running(self):
        self.transition.play()