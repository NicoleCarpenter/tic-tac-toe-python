import unittest
from lib.ttt_move_validator import TTTMoveValidator

class TestTTTMoveValidator(unittest.TestCase):

  def setUp(self):
    self.validator = TTTMoveValidator()
    self.board_size = 9
    self.active_board = ['  '] * self.board_size

  def is_valid_return(self, move):
    return self.validator.is_valid(move, self.board_size, self.active_board)

  def test_validate_move(self):
    move = '1'
    self.assertEquals(self.is_valid_return('1'), True)
    self.assertEquals(self.is_valid_return('0'), False)
    self.assertEquals(self.is_valid_return('-1'), False)
    self.assertEquals(self.is_valid_return('1.5'), False)
    self.assertEquals(self.is_valid_return('10'), False)
    self.assertEquals(self.is_valid_return('a'), False)
    self.assertEquals(self.is_valid_return('!'), False)
    self.assertEquals(self.is_valid_return(''), False)
    self.assertEquals(self.is_valid_return(' '), False)
    
    self.active_board = [' X', '  ', '  ''  ', '  ', '  ', '  ', '  ']
    self.assertEquals(self.is_valid_return('1'), False)