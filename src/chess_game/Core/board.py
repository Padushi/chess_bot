print("\n\033[95mboard.py is initialized \033[0m")
class Board():

	def __init__(self,state):
		'''
		State in Forsyth-Edwards Notation(FEN)
		'''

		self.state = state
		self.board = self.board_from_fen()
		fields = self.state.split()
		self.to_move = fields[1]


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
	
	def __str__(self):
		board_string = '''    a   b   c   d   e   f   g   h\n  +---+---+---+---+---+---+---+---+\n'''
		for i in range(8):
			board_string += f'{8-i} | {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]} | {self.board[i][3]} | {self.board[i][4]} | {self.board[i][5]} | {self.board[i][6]} | {self.board[i][7]} | {8-i}\n'
			board_string += '  +---+---+---+---+---+---+---+---+\n'
		board_string += f'    a   b   c   d   e   f   g   h'


		if self.to_move == 'w':
			board_string += "\n\nWhite to move\n"
		elif self.to_move == 'b':
			board_string += "\n\nBlack to move\n"

		return board_string
	