#player.py
import random

class Player:
    def _init_(self, marker):
        self.marker = marker

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def _init_(self, marker):
        super()._init_(marker)

    def get_move(self, game):
        while True:
            try:
                move = int(input("Enter your move (1-9): "))
                if move in game.available_moves():
                    return move
                else:
                    print("Invalid move. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

class RandomComputerPlayer(Player):
    def _init_(self, marker):
        super()._init_(marker)

    def get_move(self, game):
        return random.choice(game.available_moves())

class SmartComputerPlayer(Player):
    def _init_(self, marker):
        super()._init_(marker)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            return random.choice(game.available_moves())
        else:
            best_move = self.minimax(game, self.marker)['position']
            return best_move

    def minimax(self, state, player):
        max_player = self.marker
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                    state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -float('inf')}
        else:
            best = {'position': None, 'score': float('inf')}

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)

            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best
