import unittest
from lib.mock_view import MockView
from lib.human_move_generator import HumanMoveGenerator

class TestHumanMoveGenerator(unittest.TestCase):

  def setUp(self):
    self.view = MockView()
    self.move_generator = HumanMoveGenerator(self.view)

  def test_view(self):
    self.assertEquals(self.move_generator.view, self.view)

  def test_select_space(self):
    board_size = 9
    active_board = ['  '] * board_size
    self.view.stub_get_player_move('5')
    move = self.move_generator.select_space(board_size, active_board)
    self.assertEquals(self.view.get_player_move_called, True)
    self.assertEquals(self.view.get_player_move_called_with, [board_size, active_board])
    self.assertEquals(move, '5')