import abc

class MoveGenerator(object):
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def select_space(self, board_size, active_board):
    pass
