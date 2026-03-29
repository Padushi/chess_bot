print("\n\033[95mboard.py is initialized \033\n[0m")
import pieces

class Board():

	def __init__(self,state):
		'''
		State in Forsyth-Edwards Notation(FEN)
		'''

		self.state = state
		self.position = self.position_from_fen()

	def position_from_fen(self):

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
			print(f"| {self.position[i][0]} | {self.position[i][1]} | {self.position[i][2]} | {self.position[i][3]} | {self.position[i][4]} | {self.position[i][5]} | {self.position[i][6]} | {self.position[i][7]} | {i+1}")
		print(f"+---+---+---+---+---+---+---+---+")
		print("  h   g   f   e   d   c   b   a")





# default_board = Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')	

# print(default_board.state)
# default_board.print_board_from_position()
			
