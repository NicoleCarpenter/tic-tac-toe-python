import unittest
from lib.ttt_setup import TTTSetup
from lib.mock_view import MockView
from lib.player_builder import PlayerBuilder
from lib.human_player import HumanPlayer
from lib.computer_player import ComputerPlayer
from lib.human_move_generator import HumanMoveGenerator
from lib.computer_move_generator import ComputerMoveGenerator

class TestTTTSetup(unittest.TestCase):

  def setUp(self):
    view = MockView()
    human_move_generator = HumanMoveGenerator(view)
    computer_move_generator = ComputerMoveGenerator()
    player_builder = PlayerBuilder(human_move_generator, computer_move_generator)
    self.ttt_setup = TTTSetup(view, player_builder)

  def test_assign_game_mode(self):
    self.ttt_setup.view.stub_get_play_mode('1')
    self.assertEqual(self.ttt_setup.assign_play_mode(), '1')
    self.assertEqual(self.ttt_setup.view.prompt_play_mode_called, True)
    self.assertEqual(self.ttt_setup.view.get_play_mode_called, True)

  def test_assign_player_names(self):
    player_v_player_option = '1'
    self.ttt_setup.view.stub_get_player_name('Jack')
    players = self.ttt_setup.assign_player_names(player_v_player_option)
    self.assertIsInstance(players[0], HumanPlayer)
    self.assertIsInstance(players[1], HumanPlayer)
    self.assertEqual(players[0].name, 'Jack')
    self.assertEqual(self.ttt_setup.view.get_player_name_called, True)

    player_v_computer_option = '2'
    self.ttt_setup.view.stub_get_player_name('Jill')
    players = self.ttt_setup.assign_player_names(player_v_computer_option)
    self.assertIsInstance(players[0], HumanPlayer)
    self.assertIsInstance(players[1], ComputerPlayer)
    self.assertEqual(players[0].name, 'Jill')
    self.assertEqual(self.ttt_setup.view.get_player_name_called, True)


