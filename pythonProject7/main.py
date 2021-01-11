

from board.board import Board
from functions.functions import Controller

if __name__ == '__main__':
    board=Board("data")
    controller=Controller(board)
    controller.human_vs_computer()



