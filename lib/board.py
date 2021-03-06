import abc
import config

open_space = config.OPEN_SPACE

class Board(object):

  def __init__(self, view):
    __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def place_piece(self, marker, space):
    self.active_board[space-1] = marker

  @abc.abstractmethod
  def find_open_spaces(self, board):
    return [i for i, x in enumerate(board) if x == open_space]