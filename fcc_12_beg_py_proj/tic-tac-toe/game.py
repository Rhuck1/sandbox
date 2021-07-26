class TicTacToe:
    
    def __init__(self):
        
        self.board = [' ' for _ in range(9)] # use a single list to rep 3x3 board
        self.current_winner = None # keep track of winner
        
        
    def print_board(self):
        
        for row