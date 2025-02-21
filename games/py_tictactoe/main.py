from module import *

clear()
size = input('game board size: ')
while not size.isdigit():
    clear_lines(1)
    size = input('Not an integer! Try again. Game board size: ')
size = int(size)
game = Game('','',size)

while not game.board[0].count('X') == game.board_size:
    game.refresh('X')
game.draw_board()
clear_lines(1)
print('X filled line A. Test is over.')


