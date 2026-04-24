from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Static, Header, Footer, Label

from chess_game.Core import *
from chess_game.Utilities import *
from chess_game import game

default_board = board.Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')	

# board_utils.print_board_from_position(default_board)
# print(move_generator.generate_knight_moves('g1'))
# print(move_generator.generate_knight_moves('f4'))


print(default_board)
print(board_utils.shift_file('d4', 2))
print(move_generator.generate_orthogonal_moves('d4', 4))




class MyApp(App):
	CSS_PATH = 'main.tcss'

	def compose(self) -> ComposeResult:
		main_static = Static('Welcome to my chess game!')
		default_board = board.Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')

		chess_label = Label(str(default_board), id = 'chess')
		chess_label.border_title = "Chess Board"

		yield Header()
		yield Container(main_static, id = "box")
		yield chess_label
		yield Footer()

if __name__ == "__main__":
	MyApp().run()
