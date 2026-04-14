from ..Utilities import board_utils


def generate_diagonal_moves(position, distance):
	'''
	Takes in position in algebraic notation, distance is the max amount 
	of tiles it can move, max distance of 8
	'''
	valid_files = 'abcdefgh'
	diagonal_tiles = []
	for i in range(1, distance+1):
		diagonal_tiles.append(chr(ord(position[0]) + i) + str(int(position[1]) + i))
		diagonal_tiles.append(chr(ord(position[0]) + i) + str(int(position[1]) - i))
		diagonal_tiles.append(chr(ord(position[0]) - i) + str(int(position[1]) + i))
		diagonal_tiles.append(chr(ord(position[0]) - i) + str(int(position[1]) - i))
			
	return set(filter(board_utils.position_in_board, diagonal_tiles))

def generate_orthogonal_moves(position, distance):

	orthogonal_tiles = []
	for i in range(1, distance+1):
		orthogonal_tiles.append(chr(ord(position[0]) + i) + str(position[1]))
		orthogonal_tiles.append(chr(ord(position[0]) - i) + str(position[1]))
		orthogonal_tiles.append(position[0] + str((int(position[1]) + i)%8))
		orthogonal_tiles.append(position[0] + str((int(position[1]) - i)%8))
			
	return set(filter(board_utils.position_in_board, orthogonal_tiles))

def generate_knight_moves(position):
	knight_tiles = []

	knight_tiles.append(chr(ord(position[0]) + 2) + str(int(position[1]) + 1))
	knight_tiles.append(chr(ord(position[0]) - 2) + str(int(position[1]) + 1))
	knight_tiles.append(chr(ord(position[0]) + 2) + str(int(position[1]) - 1))
	knight_tiles.append(chr(ord(position[0]) - 2) + str(int(position[1]) - 1))
	knight_tiles.append(chr(ord(position[0]) + 1) + str(int(position[1]) + 2))
	knight_tiles.append(chr(ord(position[0]) - 1) + str(int(position[1]) + 2))
	knight_tiles.append(chr(ord(position[0]) + 1) + str(int(position[1]) - 2))
	knight_tiles.append(chr(ord(position[0]) - 1) + str(int(position[1]) - 2))

	return set(filter(board_utils.position_in_board, knight_tiles))
	
def get_queen_moves(position):
	return generate_diagonal_moves(position, 8).union(generate_orthogonal_moves(position, 8))

def get_king_moves(position):
	return generate_diagonal_moves(position, 1).union(generate_orthogonal_moves(position, 1))

def get_rook_moves(position):
	return generate_orthogonal_moves(position, 8)

def get_bishop_moves(position):
	return generate_diagonal_moves(position, 8)
