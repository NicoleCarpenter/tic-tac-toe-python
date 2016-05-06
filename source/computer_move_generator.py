import abc
import random
from source.move_generator import MoveGenerator

class ComputerMoveGenerator(MoveGenerator):

  def select_space(self, board_size):
    return random.randint(1, board_size)
