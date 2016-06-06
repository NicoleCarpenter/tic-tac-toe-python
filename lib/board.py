import abc

class Board(object):

  def __init__(self):
    __metaclass__ = abc.ABCMeta
    self.board_size = board_size

  @abc.abstractmethod
  def format_board_to_string(self, board):
    pass

  @abc.abstractmethod
  def place_piece(self, marker, space):
    pass