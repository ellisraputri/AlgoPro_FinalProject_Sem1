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
    
    def scene_1_function(self, boy, boy_text, vampire, vampire_text, screen):
        boy_rect= boy.get_rect(midleft = (30, 300))
        boy_text_rect = boy_text.get_rect(midleft =(30, 450))
        vampire_rect = vampire.get_rect(midright = (980,280))
        vampire_text_rect = vampire_text.get_rect(midright=(970,450))

        if self.active_message == 1 or self.active_message == 7 or self.active_message == 10 :
            screen.blit(boy, boy_rect)
            screen.blit(boy_text, boy_text_rect)

        elif self.active_message == 4 or self.active_message == 6 or self.active_message == 8 or self.active_message == 9 or self.active_message == 11 or self.active_message == 12:
            screen.blit(vampire, vampire_rect)
            screen.blit(vampire_text, vampire_text_rect)
        
        

    
