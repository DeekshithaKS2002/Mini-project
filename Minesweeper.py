import random

class Minesweeper:
    def _init_(self, dimension, num_bombs):
        self.dimension = dimension
        self.num_bombs = num_bombs
        self.board = [[' ' for _ in range(dimension)] for _ in range(dimension)]
        self.bomb_locations = self.generate_bombs()
        self.bombs_found = 0

    def generate_bombs(self):
        locations = set()
        while len(locations) < self.num_bombs:
            row = random.randint(0, self.dimension - 1)
            col = random.randint(0, self.dimension - 1)
            locations.add((row, col))
        return locations

    def display_board(self):
        print("   " + "  ".join(str(i) for i in range(self.dimension)))
        for i in range(self.dimension):
            print(str(i) + " |" + " |".join(self.board[i]) + " |")
            print("  +" + "---+" * (self.dimension - 1))

    def dig_cell(self, row, col):
        if (row, col) in self.bomb_locations:
            self.board[row][col] = 'X'
            self.display_board()
            print("Game Over! You hit a bomb.")
            return False
        else:
            bombs_nearby = self.count_bombs_nearby(row, col)
            self.board[row][col] = str(bombs_nearby) if bombs_nearby > 0 else ' '
            self.display_board()
            if bombs_nearby == 0:
                self.reveal_empty_cells(row, col)
            if self.dimension ** 2 - self.num_bombs == sum(row.count(' ') for row in self.board):
                print("Congratulations! You won!")
                return False
            return True

    def count_bombs_nearby(self, row, col):
        count = 0
        for i in range(max(0, row - 1), min(self.dimension, row + 2)):
            for j in range(max(0, col - 1), min(self.dimension, col + 2)):
                if (i, j) != (row, col) and (i, j) in self.bomb_locations:
                    count += 1
        return count

    def reveal_empty_cells(self, row, col):
        for i in range(max(0, row - 1), min(self.dimension, row + 2)):
            for j in range(max(0, col - 1), min(self.dimension, col + 2)):
                if self.board[i][j] == ' ':
                    bombs_nearby = self.count_bombs_nearby(i, j)
                    self.board[i][j] = str(bombs_nearby) if bombs_nearby > 0 else ' '
                    if bombs_nearby == 0:
                        self.reveal_empty_cells(i, j)

if _name_ == "_main_":
    dimension = int(input("Enter the dimension size of the board: "))
    num_bombs = int(input("Enter the number of bombs: "))
    game = Minesweeper(dimension, num_bombs)
    game.display_board()
    while True:
        row, col = map(int, input("Enter the row and column to dig (comma separated): ").split(","))
        if not game.dig_cell(row, col):
            break
