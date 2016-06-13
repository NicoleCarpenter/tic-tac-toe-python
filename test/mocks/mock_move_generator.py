import abc
from lib.move_generator import MoveGenerator

class MockMoveGenerator(MoveGenerator):

  def __init__(self):
    self.select_space_called = False
    self.select_space_return = ''

  def select_space(self, board):
    self.select_space_called = True
    return self.select_space_return

  def stub_select_space_return(self, select_space_return):
    self.select_space_return = select_space_return