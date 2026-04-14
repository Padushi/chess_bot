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


def print_board_from_position(self: board.Board):
	for i in range(8):
		print(f"+---+---+---+---+---+---+---+---+")
		print(f"| {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]} | {self.board[i][3]} | {self.board[i][4]} | {self.board[i][5]} | {self.board[i][6]} | {self.board[i][7]} | {8-i}")
	print(f"+---+---+---+---+---+---+---+---+")
	print("  a   b   c   d   e   f   g   h")

	if self.to_move == 'w':
		print("\nWhite to move\n")
	elif self.to_move == 'b':
		print("\nBlack to move\n")
	

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