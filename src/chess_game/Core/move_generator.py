import chess_game.Utility.board_utils


def generate_orthogonal_moves(position, distance):
	'''
	Takes in position in algebraic notation, distance is the max amount 
	of tiles it can move, max distance of 8
	'''
	valid_files = 'abcdefgh'
	orthogonal_tiles = []
	for i in range(1, distance+1):
		pass
