print("\n\033[95mboard.py is initialized \033[0m")
class Board():

	def __init__(self,state):
		'''
		State in Forsyth-Edwards Notation(FEN)
		'''

		self.state = state
		self.board = self.board_from_fen()

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







