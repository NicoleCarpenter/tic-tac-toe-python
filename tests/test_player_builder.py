import unittest
from source.player_builder import PlayerBuilder
from source.human_player import HumanPlayer
from source.computer_player import ComputerPlayer

class TestPlayerBuilder(unittest.TestCase):

  def setUp(self):
    self.player_builder = PlayerBuilder()

  def test_build_human_player(self):
    player = self.player_builder.build_human_player('Human Player')
    self.assertIsInstance(player, HumanPlayer)
    self.assertEquals(player.name, 'Human Player')

  def test_build_computer_player(self):
    player = self.player_builder.build_computer_player('Computer Player')
    self.assertIsInstance(player, ComputerPlayer)
    self.assertEquals(player.name, 'Computer Player')
