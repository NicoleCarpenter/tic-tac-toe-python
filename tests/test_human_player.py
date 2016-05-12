import unittest
from lib.mock_move_generator import MockMoveGenerator
from lib.human_player import HumanPlayer

class TestHumanPlayer(unittest.TestCase):
  
  def setUp(self):
    self.move_generator = MockMoveGenerator()
    self.player = HumanPlayer('Player 1', 'X', self.move_generator)

  def test_name(self):
    self.assertEquals(self.player.name, 'Player 1')

  def test_marker(self):
    self.assertEquals(self.player.marker, 'X')

  def test_move_generator(self):
    self.assertEquals(self.player.move_generator, self.move_generator)