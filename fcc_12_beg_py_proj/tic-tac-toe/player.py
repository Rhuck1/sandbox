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
        
        square = random.choice(game.available_moves())
        
        return square
    
    
Class HumanPlayer(Player):
    
    def __init__(self, letter):
        
        super().__init__(letter)
        
    def get_move(self, game):
        
        valid_square = False
        val = None
        
        while not valid_square:
            
            square = input(self.letter + '\'s turn. Input move (0-9):')
            # we're going to check that this is a correct value by trying to cast
            # it to an integer, and if it's not, then we say it's invalid.
            # If that spot is not available on the board, we also say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these are successful, then yay!
            except ValueError:
                print('Invalid square. Try again.')
                
        return val
    
    