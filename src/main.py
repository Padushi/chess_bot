# from chess_game.Core import move_generator
from chess_game.Core import *
from chess_game.Utilities import *

default_board = board.Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')	

board_utils.print_board_from_position(default_board.board)

print(pieces.get_queen_moves('d4'))
