print("\n\033[95mpieces.py is initialized \033[0m")
from ..Core import move_generator
from ..Utilities import board_utils

class Piece():

	def __init__(self, name, color, position, has_moved = True):
		
		self.name = name
		self.color = color
		self.position = position
		self.has_moved = has_moved
	
	def move_piece(self, new_position):
		self.position = new_position
		self.has_moved = True



def get_occupied_squares(board):
	'''
	Loops through the board, adding the position of each cell occupied 
	with a piece to a list, returns the list.
	'''
	
	occupied_squares = {}
	for rank in range(8):
		for file in range(8):
			if board[rank][file] != ' ':
				occupied_squares.update(board_utils.position_from_coordinates(rank, file))