import abc
import random
from lib.io import IO
from lib.ttt_move_validator import TTTMoveValidator
from lib.move_generator import MoveGenerator

class ComputerMoveGenerator(MoveGenerator):

  def __init__(self, validator, view):
    self.move_validator = validator
    self.view = view

  def select_space(self, board_size, active_board):
    self.__thinking_computer()
    move = random.randint(1, board_size)
    while not self.move_validator.is_valid(str(move), board_size, active_board):
      move = random.randint(1, board_size)
    return move

  def __thinking_computer(self):
    self.view.display_computer_thinking()