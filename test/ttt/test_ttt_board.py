import unittest
from lib.ttt.ttt_board import TTTBoard

class TestTTTBoard(unittest.TestCase):

  def setUp(self):
    board_size = 9
    self.board = TTTBoard(board_size)

  def tearDown(self):
    del self.board

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
