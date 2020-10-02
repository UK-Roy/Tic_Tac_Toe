import math
import random
from player import Player

class AI(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def turn(self, game):
        if len(game.available_turns()) == 9:
            square = random.choice(game.available_turns())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.available_turns():
            state.turn(possible_move, player)
            point = self.minimax(state, other_player)  # Evalute a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            point['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if point['score'] > best['score']:
                    best = point
            else:
                if point['score'] < best['score']:
                    best = point
        return best