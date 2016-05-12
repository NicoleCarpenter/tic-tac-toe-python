import unittest
from lib.player_builder import PlayerBuilder
from lib.human_player import HumanPlayer
from lib.computer_player import ComputerPlayer
from lib.mock_move_generator import MockMoveGenerator

class TestPlayerBuilder(unittest.TestCase):

  def setUp(self):
    self.mock_move_generator = MockMoveGenerator()
    self.player_builder = PlayerBuilder(self.mock_move_generator, self.mock_move_generator)

  def test_human_move_generator(self):
    self.assertEquals(self.player_builder.human_move_generator, self.mock_move_generator)

  def test_computer_move_generator(self):
    self.assertEquals(self.player_builder.computer_move_generator, self.mock_move_generator)

  def test_build_human_player(self):
    player = self.player_builder.build_human_player('Human Player', 'X')
    self.assertIsInstance(player, HumanPlayer)
    self.assertEquals(player.name, 'Human Player')
    self.assertEquals(player.marker, 'X')

  def test_build_computer_player(self):
    player = self.player_builder.build_computer_player('Computer Player', 'O')
    self.assertIsInstance(player, ComputerPlayer)
    self.assertEquals(player.name, 'Computer Player')
    self.assertEquals(player.marker, 'O')