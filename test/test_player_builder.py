import unittest
from test.mocks.mock_view import MockView
from lib.human_move_generator import HumanMoveGenerator
from lib.computer_move_generator import ComputerMoveGenerator
from lib.player_builder import PlayerBuilder
from lib.player import Player

class TestPlayerBuilder(unittest.TestCase):

  def setUp(self):
    view = MockView()
    human_move_generator = HumanMoveGenerator(view)
    computer_move_generator = ComputerMoveGenerator(view)
    self.player_builder = PlayerBuilder(human_move_generator, computer_move_generator)

  def test_build_human_player(self):
    player = self.player_builder.build_player('Human Player', 'X')
    self.assertEquals(player.name, 'Human Player')
    self.assertEquals(player.marker, 'X')
    self.assertIsInstance(player.move_generator, HumanMoveGenerator)

  def test_build_computer_player(self):
    player = self.player_builder.build_player('Computer', 'O')
    self.assertEquals(player.name, 'Computer')
    self.assertEquals(player.marker, 'O')
    self.assertIsInstance(player.move_generator, ComputerMoveGenerator)