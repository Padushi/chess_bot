import board_utils


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
			
	return list(filter(board_utils.position_in_board, diagonal_tiles))

def generate_orthogonal_moves(position, distance):

	orthogonal_tiles = []
	for i in range(1, distance+1):
		orthogonal_tiles.append(chr(ord(position[0]) + i) + str(position[1]))
		orthogonal_tiles.append(chr(ord(position[0]) - i) + str(position[1]))
		orthogonal_tiles.append(position[0] + str((int(position[1]) + i)%8))
		orthogonal_tiles.append(position[0] + str((int(position[1]) - i)%8))
			
	return list(filter(board_utils.position_in_board, orthogonal_tiles))
	
print(generate_diagonal_moves('d4', 1))
print(generate_orthogonal_moves('d4', 5))
