import board
import pieces



def position_from_coordinates(rank: int, file: int) -> str:
	return chr(104-rank) + str(file+1)

def coordinates_from_position(position: str) -> tuple[int,int]:
	'''
	ex: a1 -> (7, 0)
	ex: a2 -> (7, 1)
	ex: b1 -> (6, 0)
	ex: f5 -> (2, 4)

	a -> 7 -> 97
	b -> 6 -> 98
	c -> 5 -> 99
	'''


	return (ord('a') + 7 - ord(position[0]), int(position[1])-1)
