import unittest
from source.ttt_setup import TTTSetup
from source.mock_view import MockView
from source.player_builder import PlayerBuilder
from source.human_player import HumanPlayer
from source.computer_player import ComputerPlayer

class TestTTTSetup(unittest.TestCase):

  def setUp(self):
    self.view = MockView()
    self.player_builder = PlayerBuilder()
    self.ttt_setup = TTTSetup(self.view, self.player_builder)

  def test_assign_game_mode(self):
    self.ttt_setup.assign_play_mode()
    self.assertEqual(self.view.prompt_play_mode_called, True)
    self.assertEqual(self.view.get_play_mode_called, True)

  def test_assign_player_names(self):
    player_v_player_option = 1
    players = self.ttt_setup.assign_player_names(player_v_player_option)
    self.assertIsInstance(players[0], HumanPlayer)
    self.assertIsInstance(players[1], HumanPlayer)
    self.assertEqual(self.view.get_player_name_called, True)

    player_v_computer_option = 2
    players = self.ttt_setup.assign_player_names(player_v_computer_option)
    self.assertIsInstance(players[0], HumanPlayer)
    self.assertIsInstance(players[1], ComputerPlayer)
    self.assertEqual(self.view.get_player_name_called, True)


