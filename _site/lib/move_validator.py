import abc
from lib.input_validator import InputValidator

class MoveValidator(InputValidator):

  def is_valid(self, move, board):
    return self.__is_valid_number(move) and self.__is_valid_space(board.board_size, move) and self.__is_open_space(board.active_board, move)

  def __is_valid_space(self, board_size, move):
    return int(move) > 0 and int(move) <= board_size

  def __is_open_space(self, active_board, move):
    return active_board[int(move)-1] == '  '

  def __is_valid_number(self, move):
    empty_string = ''
    return move != empty_string and move.isdigit()
