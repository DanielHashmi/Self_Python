class Board:
    def __init__(self, turn):
        self.turn = turn
        self.steps = 0
        self.board = [[0, 1, 2],
                      [3, 4, 5],
                      [6, 7, 8]]
        
    def print_board(self):
        for row in self.board:
            print(f"{row[0]} | {row[1]} | {row[2]}")
        
    def set_player_pos(self, pos):
        pos = int(pos)
        col = pos % 3
        row = pos // 3
        
        if isinstance(self.board[row][col], int):
            self.board[row][col] = self.turn
            self.steps += 1
            return True
        
        print("Position already taken!")
        return False
        
    def check_winner(self, symbol):        
        # Rows
        for row in self.board:
            if symbol == row[0] == row[1] == row[2]:
                return symbol
                
        # Cols
        for i in range(0, 3):
            if symbol == self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return symbol
        
        # Diagonals
        if symbol == self.board[0][0] == self.board[1][1] == self.board[2][2]:
                return symbol
        elif symbol == self.board[0][2] == self.board[1][1] == self.board[2][0]:
                return symbol
                
        return None
            
class Player:
    def __init__(self, symbol):
        self.symbol = symbol

class Game:
    def play(self):
        playerX = Player("X")
        playerO = Player("O")
        board = Board(playerX.symbol)
        
        while True:
            try:
                board.print_board()
                pos = input(f"Enter a position for player{board.turn}: ")
                is_pos_set = board.set_player_pos(pos)
                winner = board.check_winner(board.turn)
                if winner:
                    board.print_board()
                    print(f"The winner is: {winner}")
                    break
                
                if not winner and board.steps == 9:
                    board.print_board()
                    print("Tie!")
                    break
                
                if is_pos_set:
                    if board.turn == playerX.symbol:
                        board.turn = playerO.symbol
                    else:
                        board.turn = playerX.symbol
            except ValueError:
                print("Kindly enter a Number!")
            except Exception as e:
                print(e)
                
def main():
    game = Game()
    game.play()

if __name__ == "__main__":
    main()