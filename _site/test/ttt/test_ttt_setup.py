import unittest
from test.mocks.mock_view import MockView
from lib.player_builder import PlayerBuilder
from lib.human_move_generator import HumanMoveGenerator
from lib.computer_move_generator import ComputerMoveGenerator
from lib.move_validator import MoveValidator
from lib.ttt.ttt_setup import TTTSetup

class TestTTTSetup(unittest.TestCase):
  def setUp(self):
    self.view = MockView()
    move_validator = MoveValidator()
    human_move_generator = HumanMoveGenerator(self.view)
    computer_move_generator = ComputerMoveGenerator(self.view)
    player_builder = PlayerBuilder(human_move_generator, computer_move_generator)
    self.view.stub_get_player_name('Player 1')
    self.player_vs_player = '1'
    self.player_vs_computer = '2'
    self.select_X = '1'
    self.select_O = '2'
    self.select_order = '1'
    self.random_order = '2'
    self.first_player = '1'
    self.second_player = '2'
    self.setup = TTTSetup(self.view, player_builder)

  def test_setup_game_players_pvc_X_first(self):
    setup_options = [self.player_vs_computer, self.select_X, self.select_order, self.first_player]
    self.view.stub_numbered_option_selection(setup_options)
    players = self.setup.setup_game_players()

    self.assertEquals(self.view.clear_screen_called, True)
    self.assertEquals(self.view.prompt_numbered_options_called, True)
    self.assertEquals(self.view.get_numbered_option_selection_called, True)
    self.assertIsInstance(players[0].move_generator, HumanMoveGenerator)
    self.assertIsInstance(players[1].move_generator, ComputerMoveGenerator)
    self.assertEquals(players[0].name, 'Player 1')
    self.assertEquals(players[1].name, 'Computer')
    self.assertEquals(self.view.get_player_name_called, True)
    self.assertEquals(self.view.get_player_name_called_with, 'First')
    self.player_name_return = 'Player 1'
    self.assertEquals(self.view.display_coin_flip_called, False)
    self.assertEquals(self.view.display_player_order_called, True)
    self.assertEquals(self.view.display_player_order_called_with, players[0].name)
    self.assertEquals(players[0].marker, 'X')

  def test_setup_game_players_pvc_O_first(self):
    setup_options = [self.player_vs_computer, self.select_O, self.select_order, self.first_player]
    self.view.stub_numbered_option_selection(setup_options)
    players = self.setup.setup_game_players()

    self.assertEquals(self.view.clear_screen_called, True)
    self.assertEquals(self.view.prompt_numbered_options_called, True)
    self.assertEquals(self.view.get_numbered_option_selection_called, True)
    self.assertIsInstance(players[0].move_generator, HumanMoveGenerator)
    self.assertIsInstance(players[1].move_generator, ComputerMoveGenerator)
    self.assertEquals(players[0].name, 'Player 1')
    self.assertEquals(players[1].name, 'Computer')
    self.assertEquals(self.view.get_player_name_called, True)
    self.assertEquals(self.view.get_player_name_called_with, 'First')
    self.player_name_return = 'Player 1'
    self.assertEquals(self.view.display_coin_flip_called, False)
    self.assertEquals(self.view.display_player_order_called, True)
    self.assertEquals(self.view.display_player_order_called_with, players[0].name)
    self.assertEquals(players[0].marker, 'O')

  def test_setup_game_players_pvc_X_second(self):
    setup_options = [self.player_vs_computer, self.select_X, self.select_order, self.second_player]
    self.view.stub_numbered_option_selection(setup_options)
    players = self.setup.setup_game_players()

    self.assertEquals(self.view.clear_screen_called, True)
    self.assertEquals(self.view.prompt_numbered_options_called, True)
    self.assertEquals(self.view.get_numbered_option_selection_called, True)
    self.assertIsInstance(players[0].move_generator, ComputerMoveGenerator)
    self.assertIsInstance(players[1].move_generator, HumanMoveGenerator)
    self.assertEquals(players[0].name, 'Computer')
    self.assertEquals(players[1].name, 'Player 1')
    self.assertEquals(self.view.get_player_name_called, True)
    self.assertEquals(self.view.get_player_name_called_with, 'First')
    self.player_name_return = 'Player 1'
    self.assertEquals(self.view.display_coin_flip_called, False)
    self.assertEquals(self.view.display_player_order_called, True)
    self.assertEquals(self.view.display_player_order_called_with, players[0].name)
    self.assertEquals(players[0].marker, 'O')

  def test_setup_game_players_pvc_O_second(self):
    setup_options = [self.player_vs_computer, self.select_O, self.select_order, self.second_player]
    self.view.stub_numbered_option_selection(setup_options)
    players = self.setup.setup_game_players()

    self.assertEquals(self.view.clear_screen_called, True)
    self.assertEquals(self.view.prompt_numbered_options_called, True)
    self.assertEquals(self.view.get_numbered_option_selection_called, True)
    self.assertIsInstance(players[0].move_generator, ComputerMoveGenerator)
    self.assertIsInstance(players[1].move_generator, HumanMoveGenerator)
    self.assertEquals(players[0].name, 'Computer')
    self.assertEquals(players[1].name, 'Player 1')
    self.assertEquals(self.view.get_player_name_called, True)
    self.assertEquals(self.view.get_player_name_called_with, 'First')
    self.player_name_return = 'Player 1'
    self.assertEquals(self.view.display_coin_flip_called, False)
    self.assertEquals(self.view.display_player_order_called, True)
    self.assertEquals(self.view.display_player_order_called_with, players[0].name)
    self.assertEquals(players[0].marker, 'X')

  def test_setup_game_players_pvc_X_random(self):
    setup_options = [self.player_vs_computer, self.select_X, self.random_order]
    self.view.stub_numbered_option_selection(setup_options)
    players = self.setup.setup_game_players()

    self.assertEquals(self.view.clear_screen_called, True)
    self.assertEquals(self.view.prompt_numbered_options_called, True)
    self.assertEquals(self.view.get_numbered_option_selection_called, True)
    self.assertEquals(self.view.get_player_name_called, True)
    self.assertEquals(self.view.get_player_name_called_with, 'First')
    self.player_name_return = 'Player 1'
    self.assertEquals(self.view.display_coin_flip_called, True)
    self.assertEquals(self.view.display_player_order_called, True)
    self.assertEquals(self.view.display_player_order_called_with, players[0].name)

  def test_setup_game_players_pvc_O_random(self):
    setup_options = [self.player_vs_computer, self.select_O, self.random_order]
    self.view.stub_numbered_option_selection(setup_options)
    players = self.setup.setup_game_players()

    self.assertEquals(self.view.clear_screen_called, True)
    self.assertEquals(self.view.prompt_numbered_options_called, True)
    self.assertEquals(self.view.get_numbered_option_selection_called, True)
    self.assertEquals(self.view.get_player_name_called, True)
    self.assertEquals(self.view.get_player_name_called_with, 'First')
    self.player_name_return = 'Player 1'
    self.assertEquals(self.view.display_coin_flip_called, True)
    self.assertEquals(self.view.display_player_order_called, True)
    self.assertEquals(self.view.display_player_order_called_with, players[0].name)

  def test_setup_game_players_pvp_X_first(self):
    setup_options = [self.player_vs_player, self.select_X, self.select_order, self.first_player]
    self.view.stub_numbered_option_selection(setup_options)
    players = self.setup.setup_game_players()

    self.assertEquals(self.view.clear_screen_called, True)
    self.assertEquals(self.view.prompt_numbered_options_called, True)
    self.assertEquals(self.view.get_numbered_option_selection_called, True)
    self.assertIsInstance(players[0].move_generator, HumanMoveGenerator)
    self.assertIsInstance(players[1].move_generator, HumanMoveGenerator)
    self.assertEquals(players[0].name, 'Player 1')
    self.assertEquals(players[1].name, 'Player 1')
    self.assertEquals(self.view.get_player_name_called, True)
    self.assertEquals(self.view.get_player_name_called_with, 'Second')
    self.player_name_return = 'Player 1'
    self.assertEquals(self.view.display_coin_flip_called, False)
    self.assertEquals(self.view.display_player_order_called, True)
    self.assertEquals(self.view.display_player_order_called_with, players[0].name)
    self.assertEquals(players[0].marker, 'X')

  def test_setup_game_players_pvp_O_first(self):
    setup_options = [self.player_vs_player, self.select_O, self.select_order, self.first_player]
    self.view.stub_numbered_option_selection(setup_options)
    players = self.setup.setup_game_players()

    self.assertEquals(self.view.clear_screen_called, True)
    self.assertEquals(self.view.prompt_numbered_options_called, True)
    self.assertEquals(self.view.get_numbered_option_selection_called, True)
    self.assertIsInstance(players[0].move_generator, HumanMoveGenerator)
    self.assertIsInstance(players[1].move_generator, HumanMoveGenerator)
    self.assertEquals(players[0].name, 'Player 1')
    self.assertEquals(players[1].name, 'Player 1')
    self.assertEquals(self.view.get_player_name_called, True)
    self.assertEquals(self.view.get_player_name_called_with, 'Second')
    self.player_name_return = 'Player 1'
    self.assertEquals(self.view.display_coin_flip_called, False)
    self.assertEquals(self.view.display_player_order_called, True)
    self.assertEquals(self.view.display_player_order_called_with, players[0].name)
    self.assertEquals(players[0].marker, 'O')

  def test_setup_game_players_pvp_X_second(self):
    setup_options = [self.player_vs_player, self.select_X, self.select_order, self.second_player]
    self.view.stub_numbered_option_selection(setup_options)
    players = self.setup.setup_game_players()

    self.assertEquals(self.view.clear_screen_called, True)
    self.assertEquals(self.view.prompt_numbered_options_called, True)
    self.assertEquals(self.view.get_numbered_option_selection_called, True)
    self.assertIsInstance(players[0].move_generator, HumanMoveGenerator)
    self.assertIsInstance(players[1].move_generator, HumanMoveGenerator)
    self.assertEquals(players[0].name, 'Player 1')
    self.assertEquals(players[1].name, 'Player 1')
    self.assertEquals(self.view.get_player_name_called, True)
    self.assertEquals(self.view.get_player_name_called_with, 'Second')
    self.player_name_return = 'Player 1'
    self.assertEquals(self.view.display_coin_flip_called, False)
    self.assertEquals(self.view.display_player_order_called, True)
    self.assertEquals(self.view.display_player_order_called_with, players[0].name)
    self.assertEquals(players[0].marker, 'O')

  def test_setup_game_players_pvp_O_second(self):
    setup_options = [self.player_vs_player, self.select_O, self.select_order, self.second_player]
    self.view.stub_numbered_option_selection(setup_options)
    players = self.setup.setup_game_players()

    self.assertEquals(self.view.clear_screen_called, True)
    self.assertEquals(self.view.prompt_numbered_options_called, True)
    self.assertEquals(self.view.get_numbered_option_selection_called, True)
    self.assertIsInstance(players[0].move_generator, HumanMoveGenerator)
    self.assertIsInstance(players[1].move_generator, HumanMoveGenerator)
    self.assertEquals(players[0].name, 'Player 1')
    self.assertEquals(players[1].name, 'Player 1')
    self.assertEquals(self.view.get_player_name_called, True)
    self.assertEquals(self.view.get_player_name_called_with, 'Second')
    self.player_name_return = 'Player 1'
    self.assertEquals(self.view.display_coin_flip_called, False)
    self.assertEquals(self.view.display_player_order_called, True)
    self.assertEquals(self.view.display_player_order_called_with, players[0].name)
    self.assertEquals(players[0].marker, 'X')

  def test_setup_game_players_pvp_X_random(self):
    setup_options = [self.player_vs_player, self.select_X, self.random_order]
    self.view.stub_numbered_option_selection(setup_options)
    players = self.setup.setup_game_players()

    self.assertEquals(self.view.clear_screen_called, True)
    self.assertEquals(self.view.prompt_numbered_options_called, True)
    self.assertEquals(self.view.get_numbered_option_selection_called, True)
    self.assertEquals(self.view.get_player_name_called, True)
    self.assertEquals(self.view.get_player_name_called_with, 'Second')
    self.player_name_return = 'Player 1'
    self.assertEquals(self.view.display_coin_flip_called, True)
    self.assertEquals(self.view.display_player_order_called, True)
    self.assertEquals(self.view.display_player_order_called_with, players[0].name)

  def test_setup_game_players_pvp_O_random(self):
    setup_options = [self.player_vs_player, self.select_O, self.random_order]
    self.view.stub_numbered_option_selection(setup_options)
    players = self.setup.setup_game_players()

    self.assertEquals(self.view.clear_screen_called, True)
    self.assertEquals(self.view.prompt_numbered_options_called, True)
    self.assertEquals(self.view.get_numbered_option_selection_called, True)
    self.assertEquals(self.view.get_player_name_called, True)
    self.assertEquals(self.view.get_player_name_called_with, 'Second')
    self.player_name_return = 'Player 1'
    self.assertEquals(self.view.display_coin_flip_called, True)
    self.assertEquals(self.view.display_player_order_called, True)
    self.assertEquals(self.view.display_player_order_called_with, players[0].name)