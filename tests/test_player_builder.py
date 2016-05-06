import unittest
from source.player_builder import PlayerBuilder
from source.human_player import HumanPlayer
from source.computer_player import ComputerPlayer
from source.human_move_generator import HumanMoveGenerator
from source.computer_move_generator import ComputerMoveGenerator
from source.mock_view import MockView

class TestPlayerBuilder(unittest.TestCase):

  def setUp(self):
    view = MockView()
    human_move_generator = HumanMoveGenerator(view)
    computer_move_generator = ComputerMoveGenerator()
    self.player_builder = PlayerBuilder(human_move_generator, computer_move_generator)

  def test_build_human_player(self):
    player = self.player_builder.build_human_player('Human Player')
    self.assertIsInstance(player, HumanPlayer)
    self.assertEquals(player.name, 'Human Player')

  def test_build_computer_player(self):
    player = self.player_builder.build_computer_player('Computer Player')
    self.assertIsInstance(player, ComputerPlayer)
    self.assertEquals(player.name, 'Computer Player')
