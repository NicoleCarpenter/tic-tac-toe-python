import unittest
from source.board import Board

class TestBoard(unittest.TestCase):

  def setUp(self):
    self.board_size = 9
    self.board = Board(self.board_size)

  def tearDown(self):
    del self.board

  def test_find_number_of_rows(self):
    rows = self.board.find_number_of_rows()
    self.assertEquals(rows, 3)

    self.board = Board(16)
    rows = self.board.find_number_of_rows()
    self.assertEquals(rows, 4)

  def test_separate_rows(self):
    active_board = range(1,self.board_size+1)
    separated_rows = self.board.separate_rows(active_board)
    self.assertEquals(separated_rows, [[1,2,3],[4,5,6],[7,8,9]])

    self.board_size = 16
    self.board = Board(self.board_size)
    active_board = range(1,self.board_size+1)
    separated_rows = self.board.separate_rows(active_board)
    self.assertEquals(separated_rows, [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

  def test_separate_columns(self):
    active_board = range(1, self.board_size+1)
    separated_columns = self.board.separate_columns(active_board)
    self.assertEquals(separated_columns, [[1, 4, 7], [2, 5, 8], [3, 6, 9]])

    self.board_size = 16
    self.board = Board(self.board_size)
    active_board = range(1, self.board_size+1)
    separated_columns = self.board.separate_columns(active_board)
    self.assertEquals(separated_columns, [[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,16]])

  def test_place_piece(self):
    active_board = [' '] * self.board_size
    marker = 'X'
    self.board.place_piece(marker, 2, active_board)
    self.assertEqual(active_board[1], ' ' + marker)
