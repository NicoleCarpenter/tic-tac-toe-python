import unittest
from lib.ttt_move_validator import TTTMoveValidator

class TestTTTMoveValidator(unittest.TestCase):

  def setUp(self):
    self.validator = TTTMoveValidator()
    self.board_size = 9
    self.active_board = ['  '] * self.board_size

  def test_validate_move(self):
    move = '1'
    is_valid = self.validator.is_valid(move, self.board_size, self.active_board)
    self.assertEquals(is_valid, True)

    move = '0'
    is_valid = self.validator.is_valid(move, self.board_size, self.active_board)
    self.assertEquals(is_valid, False)

    move = '-1'
    is_valid = self.validator.is_valid(move, self.board_size, self.active_board)
    self.assertEquals(is_valid, False)

    move = '1.5'
    is_valid = self.validator.is_valid(move, self.board_size, self.active_board)
    self.assertEquals(is_valid, False)

    move = '10'
    is_valid = self.validator.is_valid(move, self.board_size, self.active_board)
    self.assertEquals(is_valid, False)

    move = 'a'
    is_valid = self.validator.is_valid(move, self.board_size, self.active_board)
    self.assertEquals(is_valid, False)

    move = '!'
    is_valid = self.validator.is_valid(move, self.board_size, self.active_board)
    self.assertEquals(is_valid, False)

    move = ''
    is_valid = self.validator.is_valid(move, self.board_size, self.active_board)
    self.assertEquals(is_valid, False)

    move = ' '
    is_valid = self.validator.is_valid(move, self.board_size, self.active_board)
    self.assertEquals(is_valid, False)

    move = '1'
    self.active_board = [' X', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
    is_valid = self.validator.is_valid(move, self.board_size, self.active_board)
    self.assertEquals(is_valid, False)