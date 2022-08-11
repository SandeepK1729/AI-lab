import numpy as np 
import random 
from colored import fg
blue = fg('blue')

class TicTacToe:
        
    def create_board(self) : 
        self.board = np.array([
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']
        ])
        self.turn = 'X' 
        
    def make_move(self, P) : 
        x, y = P 
        self.board[x][y] = self.turn 
        self.turn = 'O' if self.turn == 'X' else 'X' 
    
    def print_board(self) : 
        for i in range(len(self.board)) :
            for j in range(len(self.board)) : 
                print(self.board[i][j], end = '\t') 
            print()
    
    def evaluate(self) : 
        # is X won
        if self.is_player_won('X') : 
            return 'X'
        # is O won
        if self.is_player_won('O') : 
            return 'O'
        
        if np.any(self.board == '-'): 
            return '-1' 
        # draw
        return '-'
   
    def is_player_won(self, turn) : 
        board = self.board
        n = len(board)
        game_won = []
         
        diag_wise = True 
        prince_diag_wise = True 
        
        for i in range(n) : 
            row_wise = True 
            col_wise = True 
            
            diag_wise = diag_wise and (board[i][i] == turn)
            prince_diag_wise = prince_diag_wise and (board[i][n - 1 - i] == turn)
            
            for j in range(n) : 
                row_wise = row_wise and (board[i][j] == turn) 
                col_wise = col_wise and (board[j][i] == turn) 
                
            game_won.append(col_wise) 
            game_won.append(row_wise) 
            
        game_won.append(diag_wise) 
        game_won.append(prince_diag_wise)
        
        return any(game_won)
    
    def make_random_move(self) : 
        positions = []
        for i in range(3) : 
            for j in range(3) : 
                if self.board[i][j] == '-': 
                    positions.append((i, j))
        
        self.make_move(random.choice(positions))
    
    def position_input(self, turn) : 
        x, y = map(int, input(f"Enter {self.turn} position : ").split()) 
        x -= 1 
        y -= 1 
        
        while self.board[x][y] != '-' : 
            print(f"Invalid position, {self.board[x][y]} already exit")
            x, y = map(int, input(f"Enter {turn} position : ").split()) 
            x -= 1 
            y -= 1
            
        self.make_move((x, y)) 

    def play_game(self) : 
        self.create_board()
        print("Game intiated") 
        print(self.board, end = '\n' * 2) 
        
        while self.evaluate() == '-1' : 
            
            
            if self.turn == 'X' : 
                print(fg('red'))
                print(f"{self.turn}'s turn") 
                
                self.position_input('X') 
            else : print(f"{self.turn}'s turn") 
                print(fg('blue'))
                print(f"{self.turn}'s turn") 
                
                self.make_random_move()
            
            self.print_board()
            
        result = self.evaluate() 
        if result in ['X', 'O'] : 
            return f"{result} won the match" 
        elif result == '-':
            return "Match Draw"
        
            
if __name__ == "__main__" : 
    game = TicTacToe() 
    
    print(f"Result : {game.play_game()}")
