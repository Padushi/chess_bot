print("\n\033[95mpieces.py is initialized \033[0m")
from ..Core import move_generator

class Piece():

	def __init__(self, name, position, has_moved):
		
		self.name = name
		self.position = position
		self.has_moved = has_moved
	
	def move_piece(self, new_position):
		self.position = new_position
		self.has_moved = True

def get_queen_moves(position):
	return move_generator.generate_diagonal_moves(position, 8).union(move_generator.generate_orthogonal_moves(position, 8))

def get_king_moves(position):
	return move_generator.generate_diagonal_moves(position, 1).union(move_generator.generate_orthogonal_moves(position, 1))

def get_rook_moves(position):
	return move_generator.generate_orthogonal_moves(position, 8)

def get_bishop_moves(position):
	return move_generator.generate_diagonal_moves(position, 8)

