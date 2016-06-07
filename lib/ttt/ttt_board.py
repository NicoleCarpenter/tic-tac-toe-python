import abc
import math
from lib.board import Board

class TTTBoard(Board):

  def __init__(self, board_size):
    self.board_size = board_size
    self.active_board = ['  '] * self.board_size
    self.board_positions = self.__find_board_postions()

  def place_piece(self, marker, space):
    super(TTTBoard, self).place_piece(marker, space)

  def find_open_spaces(self):
    return super(TTTBoard, self).find_open_spaces(self.active_board)

  def is_tie_condition_met(self):
    return not '  ' in self.active_board

  def is_winning_conditions_met(self):
    winning_combinations = self.__find_winning_combinations()
    for combo in winning_combinations:
      values_at_combo_positions = self.__find_values_at_combo_positions(combo)
      if self.__has_unique_values(values_at_combo_positions) and values_at_combo_positions[0] != '  ':
        return True
    return False

  def find_winning_marker(self):
    winning_combinations = self.__find_winning_combinations()
    for combo in winning_combinations:
      values_at_combo_positions = self.__find_values_at_combo_positions(combo)
      if self.__has_unique_values(values_at_combo_positions) and values_at_combo_positions[0] != '  ':
        return values_at_combo_positions[0]

  def __find_board_postions(self):
    return range(1,self.board_size+1)

  def __find_number_of_rows(self):
    return int(math.sqrt(self.board_size))

  def __find_winning_combinations(self):
    return self.__separate_rows(self.board_positions) + self.__separate_columns(self.board_positions) + self.__separate_diagonals()

  def __separate_rows(self, board):
    rows = self.__find_number_of_rows()
    separated_rows = []
    last = 0
    while last < len(board):
      separated_rows.append(board[last:last+rows])
      last += rows
    return separated_rows

  def __separate_columns(self, board):
    rows = self.__separate_rows(board)
    return map(list, zip(*rows))

  def __separate_diagonals(self):
    rows = self.__separate_rows(self.board_positions)
    row_count = self.__find_number_of_rows()
    diagonals = []
    diagonals.append(self.__find_backwards_diagonal(rows, row_count))
    diagonals.append(self.__find_forwards_diagonal(rows, row_count))
    return diagonals

  def __find_backwards_diagonal(self, rows, row_count):
    return [rows[i][i] for i in range(row_count)]

  def __find_forwards_diagonal(self, rows, row_count):
    return [rows[i][(row_count-1)-i] for i in range(row_count)]

  def __find_values_at_combo_positions(self, combo):
    return list(self.active_board[x-1] for x in combo)

  def __has_unique_values(self, values):
    return values[1:] == values[:-1]