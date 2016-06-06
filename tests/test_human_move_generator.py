import unittest
from tests.mocks.mock_view import MockView
from lib.ttt.ttt_board import TTTBoard
from lib.human_move_generator import HumanMoveGenerator

class TestHumanMoveGenerator(unittest.TestCase):

  def setUp(self):
    self.view = MockView()
    self.move_generator = HumanMoveGenerator(self.view)

  def test_select_space(self):
    board_size = 9
    player_marker = 'X'
    board = TTTBoard(board_size)
    self.view.stub_get_player_move('5')
    move = self.move_generator.select_space(board, player_marker)
    self.assertEquals(move, '5')