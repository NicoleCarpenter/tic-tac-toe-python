import unittest
from lib.ttt.ttt_board_presenter import TTTBoardPresenter

class TestTTTBoardPresenter(unittest.TestCase):

  def setUp(self):
    self.board_presenter = TTTBoardPresenter()

  def test_format_to_board_string_standard(self):
    empty_board = ['  '] * 9
    printed_board = self.board_presenter.format_board_to_string(empty_board)
    self.assertEquals(printed_board, '   |   |  \n===+===+===\n   |   |  \n===+===+===\n   |   |  \n')

    board_positions = [' 1',' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9']
    printed_board = self.board_presenter.format_board_to_string(board_positions)
    self.assertEquals(printed_board, '  1 |  2 |  3\n===+===+===\n  4 |  5 |  6\n===+===+===\n  7 |  8 |  9\n')

  def test_format_to_board_string_large(self):
    large_board_size = 16
    empty_board = ['  '] * large_board_size
    printed_board = self.board_presenter.format_board_to_string(empty_board)
    self.assertEquals(printed_board, '   |   |   |  \n===+===+===+===\n   |   |   |  \n===+===+===+===\n   |   |   |  \n===+===+===+===\n   |   |   |  \n')

    board_positions = [' 1',' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9',' 10',' 11',' 12',' 13',' 14',' 15',' 16']
    printed_board = self.board_presenter.format_board_to_string(board_positions)
    self.assertEquals(printed_board, '  1 |  2 |  3 |  4\n===+===+===+===\n  5 |  6 |  7 |  8\n===+===+===+===\n  9 |  10 |  11 |  12\n===+===+===+===\n  13 |  14 |  15 |  16\n')

  def test_find_printable_board_positions_standard(self):
    board_positions = [1,2,3,4,5,6,7,8,9]
    string_positions = self.board_presenter.find_printable_board_positions(board_positions)
    self.assertEquals(string_positions, ['1','2','3','4','5','6','7','8','9'])

  def test_find_printable_board_positions_large(self):
    board_positions = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    string_positions = self.board_presenter.find_printable_board_positions(board_positions)
    self.assertEquals(string_positions, ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16'])