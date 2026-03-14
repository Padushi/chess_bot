import pygame
import time



def draw_board(current_board):
    '''
    Uses Forsyth-Edwards Notation
    https://www.chessprogramming.org/Forsyth-Edwards_Notation
    lowercase = black piece
    uppercase = white piece
    '''

    current_board = current_board.split()

    board = [[' ',' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',' ',]]
    
    pieces = {'r': chr(9820),'n': chr(9822),'b': chr(9821),'q': chr(9819),'k': chr(9818), 'p': chr(9823),
              'R': chr(9814),'N': chr(9816),'B': chr(9815),'Q': chr(9813),'K': chr(9812), 'P': chr(9817),}
    # initializing current board
   
    col = 0
    row = 0

    for i in current_board[0]:
        if i.isdigit(): 
            col += int(i)
        elif i in pieces:
            board[row][col] = pieces[i]
            col += 1

        if col == 8:
            row += 1
            col = 0


    for i in range(8):
        print(f"+---+---+---+---+---+---+---+---+")
        print(f"| {board[i][0]} | {board[i][1]} | {board[i][2]} | {board[i][3]} | {board[i][4]} | {board[i][5]} | {board[i][6]} | {board[i][7]} |")
    print(f"+---+---+---+---+---+---+---+---+")

    return None


draw_board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
print("\n")
time.sleep(1)
draw_board("rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1")
print("\n")
time.sleep(1)
draw_board("rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w KQkq c6 0 2")
print("\n")





