from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Static, Header, Footer, Label

from chess_game.Core import *
from chess_game.Utilities import *
from chess_game import game
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
