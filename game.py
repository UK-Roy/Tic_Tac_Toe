import math
import time
from ai import AI
from human import Human
from tic_tac_toe import TicTacToe

def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.turn(game)
        else:
            square = x_player.turn(game)
        
        game.print_board_nums()
        if game.turn(square, letter):
            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')



if __name__ == '__main__':
    letter = None
    while letter != 'X' and letter != 'O':
        letter = input("Select Your letter. X or O\n")
        letter = letter.upper()

    if letter == 'X':
        x_player = Human('X')
        o_player = AI('O')
    else:
        x_player = AI('X')
        o_player = Human('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)