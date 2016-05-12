import unittest
from lib.ttt_move_validator import TTTMoveValidator
from lib.mock_view import MockView
from lib.computer_move_generator import ComputerMoveGenerator

class TestComputerMoveGenerator(unittest.TestCase):

  def setUp(self):
    self.validator = TTTMoveValidator()
    self.view = MockView()
    self.move_generator = ComputerMoveGenerator(self.validator, self.view)
    self.active_board = ['  '] * 9

  def test_move_validator(self):
    self.assertEquals(self.move_generator.move_validator, self.validator)

  def test_view(self):
    self.assertEquals(self.move_generator.view, self.view)

  def test_select_space(self):
    board_size = 9
    move = self.move_generator.select_space(board_size, self.active_board)
    self.assertTrue(move >= 1 and move <= board_size)
    self.assertEquals(self.view.display_computer_thinking_called, True)

    self.active_board = ['  ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    move = self.move_generator.select_space(board_size, self.active_board)
    self.assertEquals(move, 1)

    self.active_board = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '  ']
    move = self.move_generator.select_space(board_size, self.active_board)
    self.assertEquals(move, 9)