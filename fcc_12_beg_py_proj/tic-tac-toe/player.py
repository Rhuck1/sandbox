import math
import random


Class Player:
    
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter
        
    # we want all players to get their next move given a game
    def get_move(self, game):
        pass
    
Class RandomComputerPlayer(Player):
    
    def __init__(self, letter):
        
        super().__init__(letter)
        
    def get_move(self, game):
        pass
    
    
Class HumanPlayer(Player):
    
    def __init__(self, letter):
        
        super().__init__(letter)
        
    def get_move(self, game):
        pass
    
    