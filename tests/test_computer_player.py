import unittest
from lib.mock_move_generator import MockMoveGenerator
from lib.computer_player import ComputerPlayer

class TestHumanPlayer(unittest.TestCase):
  
  def setUp(self):
    self.move_generator = MockMoveGenerator()
    self.player = ComputerPlayer('Computer', 'O', self.move_generator)

  def test_name(self):
    self.assertEquals(self.player.name, 'Computer')

  def test_marker(self):
    self.assertEquals(self.player.marker, 'O')

  def test_move_generator(self):
    self.assertEquals(self.player.move_generator, self.move_generator)