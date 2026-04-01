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

def board_from_fen(self):

		fen = self.state.split()
		board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#h1
				[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], #g1 
				[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], #f1 
				[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], #e1 
				[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], #d1 
				[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], #c1 
				[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], #b1 
				[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']] #a1 a2 a3 a4 a5 a6 a7 a8
		
		col = 0
		row = 0

		for i in fen[0]:
			if i.isdigit():
				col += int(i)
			elif i.lower() in 'rnbqkp':
				board[row][col] = i
				col += 1

			if col == 8:
				row += 1
				col = 0
		return board
	
	

def print_board_from_position(self):
	for i in range(8):
		print(f"+---+---+---+---+---+---+---+---+")
		print(f"| {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]} | {self.board[i][3]} | {self.board[i][4]} | {self.board[i][5]} | {self.board[i][6]} | {self.board[i][7]} | {i+1}")
	print(f"+---+---+---+---+---+---+---+---+")
	print("  h   g   f   e   d   c   b   a")

def position_in_board(position):
	'''
	Returns True if position in algebraic notation is a valid cell in 
	the chess board
	'''

	return ord(position[0]) in range(ord('a'), ord('h')+1) and int(position[1]) in range(1,9)

