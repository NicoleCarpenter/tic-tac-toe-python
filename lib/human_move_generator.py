import abc
import random
from lib.move_generator import MoveGenerator

class HumanMoveGenerator(MoveGenerator):

  def __init__(self, view):
    self.view = view

  def select_space(self, board_size):
    return self.view.get_player_move(board_size)
