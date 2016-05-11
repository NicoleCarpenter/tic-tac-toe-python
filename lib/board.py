import abc
import math

class Board(object):

  def __init__(self, board_size):
    __metaclass__ = abc.ABCMeta
    self.board_size = board_size

  @abc.abstractmethod
  def find_number_of_rows(self):
    return int(math.sqrt(self.board_size))

  @abc.abstractmethod
  def separate_rows(self, board):
    rows = self.find_number_of_rows()
    separated_rows = []
    last = 0
    while last < len(board):
      separated_rows.append(board[last:last+rows])
      last += rows
    return separated_rows

  @abc.abstractmethod
  def separate_columns(self, board):
    rows = self.separate_rows(board)
    return map(list, zip(*rows))

  @abc.abstractmethod
  def format_board_to_string(self, board):
    pass

  @abc.abstractmethod
  def place_piece(self, marker, space, active_board):
    active_board[space-1] = (' ' + str(marker))
    return active_board
