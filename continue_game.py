class ContinueGame():
    def __init__(self, all_functions):
        self.all_functions = all_functions
    
    def getPosition(self, position):
        return self.all_functions[position]