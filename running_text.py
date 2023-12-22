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
    
