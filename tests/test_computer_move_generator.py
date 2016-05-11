import unittest
from lib.ttt_move_validator import TTTMoveValidator
from lib.computer_move_generator import ComputerMoveGenerator

class TestComputerMoveGenerator(unittest.TestCase):

  def setUp(self):
    validator = TTTMoveValidator()
    self.move_generator = ComputerMoveGenerator(validator)
    self.active_board = ['  '] * 9

  def test_select_space(self):
    board_size = 9
    move = self.move_generator.select_space(board_size, self.active_board)
    self.assertTrue(move >= 1 and move <= board_size)

    self.active_board = ['  ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    move = self.move_generator.select_space(board_size, self.active_board)
    self.assertEquals(move, 1)

    self.active_board = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '  ']
    move = self.move_generator.select_space(board_size, self.active_board)
    self.assertEquals(move, 9)