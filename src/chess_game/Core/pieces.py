print("\n\033[95mpieces.py is initialized \033[0m")
from ..Core import move_generator
from ..Utilities import board_utils

class Piece():

	def __init__(self, name, position):
		
		self.name = name
		self.position = position
		if self.name.isupper():
			self.color = 'w'
		else:
			self.color = 'b'
			
	def __repr__(self):
		if self.color == 'w':
			color = "White"
		else:
			color = "Black"
		return(f'\nPiece type: {self.name}, Position: {self.position}, Color: {color}')
	
	def move_piece(self, new_position):
		self.position = new_position

def get_occupied_squares(board):
	'''
	Loops through the board, adding the position of each cell occupied 
	with a piece to a list, returns the list.
	'''
	
	occupied_squares = set()
	for file in range(8):
		for rank in range(8):
			if board[file][rank] != ' ':
				occupied_squares.add(board_utils.position_from_coordinates(rank, file))
	return occupied_squares

def get_piece_list(board):
	occupied_squares = get_occupied_squares(board)
	piece_list = []

	for i in occupied_squares:
		coordinates = board_utils.coordinates_from_position(i)
		piece_list.append(Piece(board[coordinates[0]][coordinates[1]], i))

	return piece_list


	

