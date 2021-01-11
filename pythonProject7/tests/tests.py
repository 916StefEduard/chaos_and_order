

from board.board import Board
from functions.functions import Controller
import unittest

class Tests(unittest.TestCase):

    def test_board(self):
        board=Board("data")
        board.move_player(1,1,'X')
        board.move_player(1,2, 'X')
        board.move_player(1,3, 'X')
        board.move_player(1,4, 'X')
        board.move_computer()
        assert board.is_game_won()==False
        assert board.is_board_full()==False
        assert board.get_slot(1,5)!='O'

