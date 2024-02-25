#game.py
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def _init_(self):
        self.board = [' ' for _ in range(9)]  # 3x3 board represented as a list

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def winner(self, marker):
        # Check rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            if all(spot == marker for spot in row):
                return True

        # Check columns
        for col in [self.board[i::3] for i in range(3)]:
            if all(spot == marker for spot in col):
                return True

        # Check diagonals
        diagonals = [[self.board[i] for i in [0, 4, 8]], [self.board[i] for i in [2, 4, 6]]]
        if any(all(spot == marker for spot in diagonal) for diagonal in diagonals):
            return True

        return False

    def full_board(self):
        return ' ' not in self.board

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def play(self, x_player, o_player):
        current_player = x_player
        while not (self.winner('X') or self.winner('O') or self.full_board()):
            self.print_board()
            if current_player == x_player:
                move = x_player.get_move(self)
                self.board[move - 1] = 'X'
                current_player = o_player
            else:
                move = o_player.get_move(self)
                self.board[move - 1] = 'O'
                current_player = x_player

        self.print_board()
        if self.winner('X'):
            print("X wins!")
        elif self.winner('O'):
            print("O wins!")
        else:
            print("It's a tie!")

if _name_ == "_main_":
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    game = TicTacToe()
    game.play(x_player, o_player)
