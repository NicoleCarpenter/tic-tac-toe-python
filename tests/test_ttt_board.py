import unittest
from source.ttt_board import TTTBoard

class TestTTTBoard(unittest.TestCase):

  def setUp(self):
    self.board = TTTBoard()

  def tearDown(self):
    del self.board

  def test_format_to_board_string(self):
    board = ['  '] * 9
    rows = self.board.format_board_to_string(board)
    self.assertEquals(rows, '   |   |  \n===+===+===\n   |   |  \n===+===+===\n   |   |  \n')
