import unittest
from lib.computer_move_generator import ComputerMoveGenerator

class TestComputerMoveGenerator(unittest.TestCase):

  def setUp(self):
    self.move_generator = ComputerMoveGenerator()

  def test_select_space(self):
    board_size = 9
    move = self.move_generator.select_space(board_size)
    self.assertTrue(move >= 1 and move <= board_size)
