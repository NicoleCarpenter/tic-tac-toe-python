import abc

class MoveGenerator(object):
  __metaclass__ = abc.ABCMeta
  self.view = view

  @abc.abstractmethod
  def select_space(self, board):
    pass