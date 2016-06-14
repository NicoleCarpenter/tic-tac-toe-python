import unittest
import config
from lib.ttt.ttt_board import TTTBoard
from lib.move_validator import MoveValidator

xxx = config.OPEN_SPACE

class TestMoveValidator(unittest.TestCase):

  def setUp(self):
    self.validator = MoveValidator()
    board_size = 9
    self.board = TTTBoard(board_size)

  def is_valid_return(self, move):
    return self.validator.is_valid(move, self.board)

  def test_validate_move(self):
    move = '1'
    self.assertEquals(self.is_valid_return('1'), True)

  def test_validate_move_fail_number(self):
    self.assertEquals(self.is_valid_return('0'), False)
    self.assertEquals(self.is_valid_return('-1'), False)
    self.assertEquals(self.is_valid_return('1.5'), False)
    self.assertEquals(self.is_valid_return('10'), False)

  def test_validate_move_fail_char(self):
    self.assertEquals(self.is_valid_return('a'), False)
    self.assertEquals(self.is_valid_return('!'), False)
    self.assertEquals(self.is_valid_return(''), False)
    self.assertEquals(self.is_valid_return(' '), False)

  def test_validate_move_fail_space_taken(self):
    self.board.active_board = \
    [ 'X', xxx, xxx,
      xxx, xxx, xxx,
      xxx, xxx, xxx ]
    self.assertEquals(self.is_valid_return('1'), False)
