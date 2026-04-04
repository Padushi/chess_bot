print("\n\033[95mpieces.py is initialized \033[0m")

class Piece():

	def __init__(self, name, position, has_moved):
		
		self.name = name
		self.position = position
		self.has_moved = has_moved
	
	def move_piece(self, new_position):
		self.position = new_position
		self.has_moved = True


def add(a,b):
	return a + b
	