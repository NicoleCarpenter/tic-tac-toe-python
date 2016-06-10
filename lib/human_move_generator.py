import abc
from lib.move_generator import MoveGenerator

class HumanMoveGenerator(MoveGenerator):

  def __init__(self, view):
    self.view = view

  def select_space(self, board):
    return self.view.get_player_move(board)