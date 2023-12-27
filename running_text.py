class DialogText:
    def __init__(self, font, messages):
        self.font = font
        self.messages = messages
        self.snip = font.render('', True, 'white')
        self.counter = 0 
        self.speed = 3
        self.done = False
        self.active_message = 0
        self.message = messages[self.active_message]
    
    def running_message(self, screen):
        if self.counter < self.speed * len(self.message):
            self.counter += 1
        elif self.counter >= self.speed*len(self.message):
            self.done = True
        self.snip = self.font.render(self.message[0:self.counter//self.speed], True, 'white')
        screen.blit(self.snip, (30,525))
    
    def checking_message_done(self):
        if self.done==True and self.active_message < len(self.messages)-1:
            self.active_message +=1
            self.done = False
            self.message = self.messages[self.active_message]
            self.counter = 0
    
    def scene_1_function(self, boy, boy_text, vampire, vampire_text, scroll, screen):
        boy_rect= boy.get_rect(midleft = (30, 300))
        boy_text_rect = boy_text.get_rect(midleft =(30, 450))
        vampire_rect = vampire.get_rect(midright = (980,280))
        vampire_text_rect = vampire_text.get_rect(midright=(970,450))
        scroll_rect = scroll.get_rect(center=(500,325))

        if self.active_message == 1 or self.active_message == 7 or self.active_message == 10 :
            screen.blit(boy, boy_rect)
            screen.blit(boy_text, boy_text_rect)

        elif self.active_message == 4 or self.active_message == 6 or self.active_message == 8 or self.active_message == 9 or self.active_message == 11 or self.active_message==13:
            screen.blit(vampire, vampire_rect)
            screen.blit(vampire_text, vampire_text_rect)

        elif self.active_message == 12:
            screen.blit(scroll, scroll_rect)
    
    def scene_2_function(self, boy, boy_text, castle, screen):
        boy_rect= boy.get_rect(midleft = (30, 320))
        boy_text_rect = boy_text.get_rect(midleft =(30, 450))
        castle_rect = castle.get_rect(center=(500, 275))

        if self.active_message == 0 or self.active_message == 1 or self.active_message == 3 or self.active_message == 4 or self.active_message == 6 or self.active_message == 7 or self.active_message == 10:
            screen.blit(boy, boy_rect)
            screen.blit(boy_text, boy_text_rect)

        elif self.active_message == 9:
            screen.blit(castle,castle_rect)
    
    def scene_3_function(self, boy, boy_text, man, man_text, screen):
        boy_rect= boy.get_rect(midleft = (30, 350))
        boy_text_rect = boy_text.get_rect(midleft =(30, 450))
        man_rect = man.get_rect(midright = (980,320))
        man_text_rect = man_text.get_rect(midright=(950,450))

        if self.active_message == 0 or self.active_message == 3 or self.active_message == 4 or self.active_message == 8 or self.active_message == 11 or self.active_message == 13:
            screen.blit(boy, boy_rect)
            screen.blit(boy_text, boy_text_rect)

        elif self.active_message == 1 or self.active_message == 5 or self.active_message == 7 or self.active_message == 9 :
            screen.blit(man, man_rect)
            screen.blit(man_text, man_text_rect)
    
    def scene_4_function(self, boy, boy_text, man, man_text, screen):
        boy_rect= boy.get_rect(midleft = (30, 350))
        boy_text_rect = boy_text.get_rect(midleft =(30, 450))
        man_rect = man.get_rect(midright = (980,320))
        man_text_rect = man_text.get_rect(midright=(950,450))

        if self.active_message == 0 or self.active_message == 2 or self.active_message == 6 or self.active_message == 8 or self.active_message == 10 or self.active_message == 12:
            screen.blit(boy, boy_rect)
            screen.blit(boy_text, boy_text_rect)

        elif self.active_message == 1 or self.active_message == 3 or self.active_message == 4 or self.active_message == 5 or self.active_message == 7 or self.active_message == 9:
            screen.blit(man, man_rect)
            screen.blit(man_text, man_text_rect)
    

    def scene_5_function(self, boy, boy_text, vampire, vampire_text, screen):
        boy_rect= boy.get_rect(midleft = (30, 300))
        boy_text_rect = boy_text.get_rect(midleft =(30, 450))
        vampire_rect = vampire.get_rect(midright = (980,280))
        vampire_text_rect = vampire_text.get_rect(midright=(970,450))

        #because there is too much dialog, for this scene, the dialog will be stored in dictionary
        dialog_index = {"boy":[0,1,3,6,7,16], "vampire":[2,4,9,10,11,12,13,17,18,19,22]}

        for key,dialog_list in dialog_index.items():
            if key == "boy":
                for i in dialog_list:
                    if self.active_message == i:
                        screen.blit(boy, boy_rect)
                        screen.blit(boy_text, boy_text_rect)
            
            elif key == "vampire":
                for i in dialog_list:
                    if self.active_message == i:
                        screen.blit(vampire, vampire_rect)
                        screen.blit(vampire_text, vampire_text_rect)
    

    def scene_6_function(self, boy, boy_text, vampire, vampire_text, screen):
        boy_rect= boy.get_rect(midleft = (30, 300))
        boy_text_rect = boy_text.get_rect(midleft =(30, 450))
        vampire_rect = vampire.get_rect(midright = (980,280))
        vampire_text_rect = vampire_text.get_rect(midright=(970,450))
        
        if self.active_message == 2 or self.active_message == 4 or self.active_message == 5 or self.active_message == 7 or self.active_message == 8 or self.active_message == 10:
            screen.blit(boy, boy_rect)
            screen.blit(boy_text, boy_text_rect)

        elif self.active_message == 0:
            screen.blit(vampire, vampire_rect)
            screen.blit(vampire_text, vampire_text_rect)

        
        
        
        

    
