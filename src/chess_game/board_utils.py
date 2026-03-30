def position_from_coordinates(rank: int, file: int) -> str:
	return chr(104-rank) + str(file+1)

def coordinates_from_position(position: str) -> tuple[int,int]:
	'''
	ex: a1 -> (7, 0)
	ex: a2 -> (7, 1)
	ex: b1 -> (6, 0)
	ex: f5 -> (2, 4)
	'''

	return (ord('a') + 7 - ord(position[0]), int(position[1])-1)

def get_occupied_squares(board):
	'''
	Loops through the board, adding the position of each cell occupied 
	with a piece to a list, returns the list.
	'''
	
	occupied_squares = []
	for rank in board:
		for file in rank:
			if board[rank][file] != ' ':

				occupied_squares.append(position_from_coordinates(rank, file))

	return occupied_squares

