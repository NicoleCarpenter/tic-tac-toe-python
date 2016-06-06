import abc
from lib.validators.input_validator import InputValidator

class MoveValidator(InputValidator):

  def is_valid(self, move, board_size, active_board):
    return self.__is_valid_number(move) and self.__is_valid_space(board_size, move) and self.__is_open_space(active_board, move)

  def __is_valid_space(self, board_size, move):
    return int(move) > 0 and int(move) <= board_size

  def __is_open_space(self, active_board, move):
    return active_board[int(move)-1] == '  '

  def __is_valid_number(self, move):
    empty_string = ''
    return move != empty_string and move.isdigit()
