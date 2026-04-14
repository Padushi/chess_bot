from chess_game.Core import *
from chess_game.Utilities import *
from chess_game import game

default_board = board.Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')	

board_utils.print_board_from_position(default_board)
print(move_generator.generate_knight_moves('g1'))
# print(move_generator.generate_knight_moves('f4'))

print(board_utils.shift_file('d4', 2))
