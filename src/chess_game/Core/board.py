print("\n\033[95mboard.py is initialized \033[0m")
import pieces

class Board():

	def __init__(self,state):
		'''
		State in Forsyth-Edwards Notation(FEN)
		'''

		self.state = state
		self.board = self.board_from_fen()




default_board = Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')	

default_board.print_board_from_position()


