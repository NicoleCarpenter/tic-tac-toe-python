import unittest
from source.human_move_generator import HumanMoveGenerator
from source.mock_view import MockView

class TestHumanMoveGenerator(unittest.TestCase):

  def setUp(self):
    view = MockView()
    self.move_generator = HumanMoveGenerator(view)

  def test_select_space(self):
    self.move_generator.view.stub_get_player_move('5')
    board_size = 9
    move = self.move_generator.select_space(board_size)
    self.assertEquals(self.move_generator.view.get_player_move_called, True)
    self.assertEquals(move, '5')
    self.assertTrue(int(move) >= 1 and int(move) <= board_size)
