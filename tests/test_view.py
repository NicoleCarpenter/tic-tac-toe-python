import unittest
from source.view import View
from source.mock_io import MockIO

class TestView(unittest.TestCase):

  def setUp(self):
    self.io = MockIO()
    self.view = View(self.io)

  def test_prompt_play_mode(self):
    self.view.prompt_play_mode()
    self.assertEqual(self.io.display_called, True)
    self.assertEqual(self.io.output_stream, '2 - Player vs Computer')

  def test_get_play_mode(self):
    self.io.stubbed_user_input = '1'
    self.assertEqual(self.view.get_play_mode(), '1')
    self.assertEqual(self.io.get_user_input_called, True)

  def test_get_player_move(self):
    self.io.stubbed_user_input = '2'
    board_size = 9
    self.assertEqual(self.view.get_player_move(board_size), '2')
    self.assertEqual(self.io.get_user_input_called, True)
