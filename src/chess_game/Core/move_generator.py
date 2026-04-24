from ..Utilities import board_utils


def generate_diagonal_moves(position, distance):
	'''
	Takes in position in algebraic notation, distance is the max amount 
	of tiles it can move, max distance of 8
	'''
	valid_files = 'abcdefgh'
	diagonal_tiles = []
	for i in range(1, distance+1):

		diagonal_tiles.append(board_utils.shift_file(board_utils.shift_rank(position, i), i))
		diagonal_tiles.append(board_utils.shift_file(board_utils.shift_rank(position, i), -i))
		diagonal_tiles.append(board_utils.shift_file(board_utils.shift_rank(position, -i), i))
		diagonal_tiles.append(board_utils.shift_file(board_utils.shift_rank(position, -i), -i))
			
	return set(filter(board_utils.position_in_board, diagonal_tiles))

def generate_orthogonal_moves(position, distance):

	orthogonal_tiles = []
	for i in range(1, distance+1):

		orthogonal_tiles.append(board_utils.shift_file(position, i))
		orthogonal_tiles.append(board_utils.shift_file(position, -i))
		orthogonal_tiles.append(board_utils.shift_rank(position, i))
		orthogonal_tiles.append(board_utils.shift_rank(position, -i))
			
	return set(filter(board_utils.position_in_board, orthogonal_tiles))

def generate_knight_moves(position):
	knight_tiles = []
	knight_tiles.append(board_utils.shift_file(board_utils.shift_rank(position, 1), 2))
	knight_tiles.append(board_utils.shift_file(board_utils.shift_rank(position, 1), -2))
	knight_tiles.append(board_utils.shift_file(board_utils.shift_rank(position, -1), 2))
	knight_tiles.append(board_utils.shift_file(board_utils.shift_rank(position, -1), -2))

	knight_tiles.append(board_utils.shift_rank(board_utils.shift_file(position, 1), 2))
	knight_tiles.append(board_utils.shift_rank(board_utils.shift_file(position, 1), -2))
	knight_tiles.append(board_utils.shift_rank(board_utils.shift_file(position, -1), 2))
	knight_tiles.append(board_utils.shift_rank(board_utils.shift_file(position, -1), -2))

	return set(filter(board_utils.position_in_board, knight_tiles))

def generate_pawn_moves(position, color, board):
	pawn_tiles = []
	if color == 'w':
		pawn_tiles.append(board_utils.shift_rank(position, 1))
		if position[1] == '2':
			pawn_tiles.append(board_utils.shift_rank(position, 2))
	else:
		pawn_tiles.append(board_utils.shift_rank(position, -2))
		if position[1] == '7':
			pawn_tiles.append(board_utils.shift_rank(position, -1))

	return set(filter(board_utils.position_in_board, pawn_tiles))
	

			
			


def get_queen_moves(position):
	return generate_diagonal_moves(position, 8).union(generate_orthogonal_moves(position, 8))

def get_king_moves(position):
	return generate_diagonal_moves(position, 1).union(generate_orthogonal_moves(position, 1))

def get_rook_moves(position):
	return generate_orthogonal_moves(position, 8)

def get_bishop_moves(position):
	return generate_diagonal_moves(position, 8)
