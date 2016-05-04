import unittest
from source.ttt_setup import TTTSetup
from source.mock_view import MockView

class TestTTTSetup(unittest.TestCase):

  def setUp(self):
    self.view = MockView()
    self.ttt_setup = TTTSetup(self.view)

  def test_assign_game_mode(self):
    self.ttt_setup.assign_play_mode()
    self.assertEqual(self.view.prompt_play_mode_called, True)
    self.assertEqual(self.view.get_play_mode_called, True)
