import unittest
from lib.mock_view import MockView
from lib.player_builder import PlayerBuilder
from lib.human_player import HumanPlayer
from lib.computer_player import ComputerPlayer
from lib.ttt_move_validator import TTTMoveValidator
from lib.mock_move_generator import MockMoveGenerator
from lib.ttt_setup import TTTSetup

class TestTTTSetup(unittest.TestCase):

  def setUp(self):
    self.view = MockView()
    move_validator = TTTMoveValidator()
    move_generator = MockMoveGenerator()
    player_builder = PlayerBuilder(move_generator, move_generator)
    self.setup = TTTSetup(self.view, player_builder)

  def test_assign_play_mode(self):
    options = ['1 - Player vs Player', '2 - Player vs Computer']
    self.view.stub_get_play_mode('1')
    self.assertEquals(self.setup.assign_play_mode(), '1')
    self.assertEquals(self.view.prompt_play_mode_called, True)
    self.assertEquals(self.view.prompt_play_mode_called_with, options)
    self.assertEquals(self.view.get_play_mode_called, True)
    self.assertEquals(self.view.get_play_mode_called_with, options)

  def test_assign_player_names(self):
    player_v_player_option = '1'
    self.view.stub_get_player_name('Jack')
    players = self.setup.assign_player_names(player_v_player_option)
    self.assertIsInstance(players[0], HumanPlayer)
    self.assertIsInstance(players[1], HumanPlayer)
    self.assertEquals(players[0].name, 'Jack')
    self.assertEquals(self.view.get_player_name_called, True)
    self.assertEquals(self.view.get_player_name_called_with, 'Second')


    player_v_computer_option = '2'
    self.view.stub_get_player_name('Jill')
    players = self.setup.assign_player_names(player_v_computer_option)
    self.assertIsInstance(players[0], HumanPlayer)
    self.assertIsInstance(players[1], ComputerPlayer)
    self.assertEquals(players[0].name, 'Jill')
    self.assertEquals(players[1].name, 'Computer')
    self.assertEquals(self.view.get_player_name_called, True)
    self.assertEquals(self.view.get_player_name_called_with, 'First')

