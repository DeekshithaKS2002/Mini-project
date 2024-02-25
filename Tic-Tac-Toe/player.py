# player.py 
class Player:
    def _init_(self, marker):
        self.marker = marker

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def _init_(self, marker):
        super()._init_(marker)

    def get_move(self, game):
        import random
        return random.choice(game.available_moves())

class HumanPlayer(Player):
    def _init_(self, marker):
        super()._init_(marker)

    def get_move(self, game):
        valid_move = False
        while not valid_move:
            try:
                move = int(input("Enter your move (1-9): "))
                if move in game.available_moves():
                    valid_move = True
                    return move
                else:
                    print("Invalid move. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

if _name_ == "_main_":
    # You can add any additional setup or test code here if needed
    pass
