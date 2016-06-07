import unittest
from lib.ttt.ttt_board import TTTBoard

class TestTTTBoard(unittest.TestCase):

  def setUp(self):
    board_size = 9
    self.board = TTTBoard(board_size)

  def tearDown(self):
    del self.board

  def test_format_to_board_string_standard(self):
    empty_board = ['  '] * 9
    printed_board = self.board.format_board_to_string(empty_board)
    self.assertEquals(printed_board, '   |   |  \n===+===+===\n   |   |  \n===+===+===\n   |   |  \n')

    board_positions = [' 1',' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9']
    printed_board = self.board.format_board_to_string(board_positions)
    self.assertEquals(printed_board, '  1 |  2 |  3\n===+===+===\n  4 |  5 |  6\n===+===+===\n  7 |  8 |  9\n')

  def test_format_to_board_string_large(self):
    large_board_size = 16
    self.board = TTTBoard(large_board_size)
    
    empty_board = ['  '] * large_board_size
    printed_board = self.board.format_board_to_string(empty_board)
    self.assertEquals(printed_board, '   |   |   |  \n===+===+===+===\n   |   |   |  \n===+===+===+===\n   |   |   |  \n===+===+===+===\n   |   |   |  \n')

    board_positions = [' 1',' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9',' 10',' 11',' 12',' 13',' 14',' 15',' 16']
    printed_board = self.board.format_board_to_string(board_positions)
    self.assertEquals(printed_board, '  1 |  2 |  3 |  4\n===+===+===+===\n  5 |  6 |  7 |  8\n===+===+===+===\n  9 |  10 |  11 |  12\n===+===+===+===\n  13 |  14 |  15 |  16\n')

  def test_find_printable_board_positions_standard(self):
    board_positions = self.board.find_printable_board_positions()
    self.assertEquals(board_positions, ['1','2','3','4','5','6','7','8','9'])

  def test_find_printable_board_positions_large(self):
    board_size = 16
    self.board = TTTBoard(board_size)
    board_positions = self.board.find_printable_board_positions()
    self.assertEquals(board_positions, ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16'])

  def test_place_piece(self):
    marker = 'X'
    space = 2
    self.board.place_piece(marker, space)
    self.assertEqual(self.board.active_board[1], marker)

    marker = 'O'
    space = 9
    self.board.place_piece(marker, space)
    self.assertEqual(self.board.active_board[8], marker)

  def test_is_tie_condition_met(self): 
    self.board.active_board = ['X','X','X','X','X','X','X','X','X']
    self.assertTrue(self.board.is_tie_condition_met())

    self.board.active_board = ['O','O','O','O','O','O','O','O','O']
    self.assertTrue(self.board.is_tie_condition_met())

    self.board.active_board = ['X','X','O','X','X','O','O','O','X']
    self.assertTrue(self.board.is_tie_condition_met())

  def test_tie_condition_not_met(self):
    self.board.active_board = ['  ','X','X','X','X','X','X','X','X']
    self.assertFalse(self.board.is_tie_condition_met())

    self.board.active_board = ['  ','  ','  ','  ','  ','  ','  ','  ','  ']
    self.assertFalse(self.board.is_tie_condition_met())
  
  def test_is_winning_conditions_met_row(self):
    self.board.active_board = ['X','X','X','  ','  ','  ','  ','  ','  ']
    self.assertTrue(self.board.is_winning_conditions_met())

    self.board.active_board = ['  ','  ','  ','X','X','X','  ','  ','  ']
    self.assertTrue(self.board.is_winning_conditions_met())

    self.board.active_board = ['  ','  ','  ','  ','  ','  ','X','X','X']
    self.assertTrue(self.board.is_winning_conditions_met())

  def test_winning_conditions_met_column(self):
    self.board.active_board = ['X','  ','  ','X','  ','  ','X','  ','  ']
    self.assertTrue(self.board.is_winning_conditions_met())

    self.board.active_board = ['  ','X','  ','  ','X','  ','  ','X','  ']
    self.assertTrue(self.board.is_winning_conditions_met())

    self.board.active_board = ['  ','  ','X','  ','  ','X','  ','  ','X']
    self.assertTrue(self.board.is_winning_conditions_met())

  def test_winning_conditions_met_diagonal(self):
    self.board.active_board = ['X','  ','  ','  ','X','  ','  ','  ','X']
    self.assertTrue(self.board.is_winning_conditions_met())

    self.board.active_board = ['  ','  ','X','  ','X','  ','X','  ','  ']
    self.assertTrue(self.board.is_winning_conditions_met())

  def test_winning_conditions_not_met(self):
    self.board.active_board = ['  ','  ','  ','  ','  ','  ','  ','  ','  ']
    self.assertFalse(self.board.is_winning_conditions_met())

    self.board.active_board = ['X','O','X','  ','  ','  ','  ','  ','  ']
    self.assertFalse(self.board.is_winning_conditions_met())

  def test_find_winning_marker_row(self):
    self.board.active_board = ['X','X','X','  ','  ','  ','  ','  ','  ']
    self.assertEquals(self.board.find_winning_marker(), 'X')

    self.board.active_board = ['  ','  ','  ','X','X','X','  ','  ','  ']
    self.assertEquals(self.board.find_winning_marker(), 'X')

    self.board.active_board = ['  ','  ','  ','  ','  ','  ','X','X','X']
    self.assertEquals(self.board.find_winning_marker(), 'X')

  def test_find_winning_marker_column(self):
    self.board.active_board = ['X','  ','  ','X','  ','  ','X','  ','  ']
    self.assertEquals(self.board.find_winning_marker(), 'X')

    self.board.active_board = ['  ','X','  ','  ','X','  ','  ','X','  ']
    self.assertEquals(self.board.find_winning_marker(), 'X')

    self.board.active_board = ['  ','  ','X','  ','  ','X','  ','  ','X']
    self.assertEquals(self.board.find_winning_marker(), 'X')

  def test_find_winning_marker_diagonal(self):
    self.board.active_board = ['X','  ','  ','  ','X','  ','  ','  ','X']
    self.assertEquals(self.board.find_winning_marker(), 'X')

    self.board.active_board = ['  ','  ','X','  ','X','  ','X','  ','  ']
    self.assertEquals(self.board.find_winning_marker(), 'X')

  def test_find_winning_marker_none(self):
    self.board.active_board = ['  ','  ','  ','  ','  ','  ','  ','  ','  ']
    self.assertEquals(self.board.find_winning_marker(), None)

    self.board.active_board = ['X','O','X','  ','  ','  ','  ','  ','  ']
    self.assertEquals(self.board.find_winning_marker(), None)

  def test_find_open_spaces(self):
    self.board.active_board = ['  ','  ','  ','  ','  ','  ','  ','  ','  ']
    self.assertEquals(self.board.find_open_spaces(), [0,1,2,3,4,5,6,7,8])

    self.board.active_board = ['  ','  ','  ','X','X','X','X','X','X']
    self.assertEquals(self.board.find_open_spaces(), [0,1,2])

    self.board.active_board = ['X','X','X','X','X','X','X','X','X']
    self.assertEquals(self.board.find_open_spaces(), [])














