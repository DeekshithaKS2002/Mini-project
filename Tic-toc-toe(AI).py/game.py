#game.py
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer

class TicTacToe:
    def _init_(self):
        self.board = [' ' for _ in range(9)]  # 3x3 board represented as a list
        self.current_winner = None

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, player):
        if self.board[square] == ' ':
            self.board[square] = player
            if self.winner(square, player):
                self.current_winner = player
            return True
        return False

    def winner(self, square, player):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == player for spot in row]):
            return True

        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == player for spot in column]):
            return True

        # Check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # Left to right diagonal
            if all([spot == player for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # Right to left diagonal
            if all([spot == player for spot in diagonal2]):
                return True

        return False

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

if _name_ == "_main_":
    x_player = HumanPlayer('X')
    o_player = SmartComputerPlayer('O')
    game = TicTacToe()
    while game.empty_squares() and not game.current_winner:
        game.print_board()
        if game.current_winner:
            print(f"The winner is {game.current_winner}")
            break
        elif not game.empty_squares():
            print("It's a tie!")
            break
        else:
            square = x_player.get_move(game) if game.current_winner != 'X' else o_player.get_move(game)
            game.make_move(square, 'X' if game.current_winner != 'X' else 'O')
