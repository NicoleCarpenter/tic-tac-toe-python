import abc

class MoveGenerator(object):
  __metaclass__ = abc.ABCMeta

  def __init__(self):
    self.view = view

  @abc.abstractmethod
  def select_space(self, board):
    pass