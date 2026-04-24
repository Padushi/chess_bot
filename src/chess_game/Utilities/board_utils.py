from ..Core import *

def position_from_coordinates(rank: int, file: int) -> str:
	return chr(104-rank) + str(file+1)

def coordinates_from_position(position: str) -> tuple[int,int]:
	'''
	ex: a1 -> (7, 0)
	ex: a2 -> (7, 1)
	ex: b1 -> (6, 0)
	ex: f5 -> (2, 4)
	'''

	return (int(position[1])-1, ord('a') + 7 - ord(position[0]))

	

def position_in_board(position):
	'''
	Returns True if position in algebraic notation is a valid cell in 
	the chess board
	'''
	try:
		return ord(position[0]) in range(ord('a'), ord('h')+1) and int(position[1]) in range(1,9)
	except ValueError:
		return False

def position_is_occupied(board, position):
	return board[coordinates_from_position(position)[0]][coordinates_from_position(position)[1]]

def shift_rank(position, amount):
		return position[0] + str(int(position[1]) + amount)

def shift_file(position, amount):
	return chr(ord(position[0]) + amount) + position[1]
