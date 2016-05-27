import abc
import itertools
import math
from lib.board import Board

class TTTBoard(Board):

  def __init__(self, board_size):
    self.board_size = board_size
    self.active_board = ['  '] * self.board_size
    self.board_positions = self.__find_board_postions()

  def format_board_to_string(self, board):
    formatted_board = self.__add_leading_spaces(board)
    formatted_rows = []
    number_of_rows = self.__find_number_of_rows()
    rows = self.__separate_rows(formatted_board)
    for index, row in enumerate(rows):
      formatted_rows.append(self.__format_row(row, number_of_rows))
      self.__add_horizontal_fillers_if_between_rows(index, formatted_rows, number_of_rows)
    converted_string = self.__convert_board_list_to_string(formatted_rows)
    return converted_string

  def find_printable_board_positions(self):
    return map('{:1}'.format, self.board_positions)

  def place_piece(self, marker, space):
    self.active_board[space-1] = marker

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

  def find_open_spaces(self):
    return [i for i, x in enumerate(self.active_board) if x == '  ']

  def __find_board_postions(self):
    return range(1,self.board_size+1)

  def __add_leading_spaces(self, board):
    return [' ' + x if x!='  ' else x for x in board]

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

  def __format_row(self, row, number_of_rows):
    vertical_fillers = self.__construct_vertical_fillers(number_of_rows)
    filled_row = self.__construct_filled_row(row, vertical_fillers)
    flattened_row = self.__flatten_row(filled_row)
    formatted_with_newline = self.__append_row_with_newline(flattened_row)
    return formatted_with_newline

  def __construct_vertical_fillers(self, number_of_rows):
    return [' |'] * (number_of_rows - 1)

  def __construct_filled_row(self, row, row_fillers):
    return map(list, itertools.izip_longest(row, row_fillers))

  def __flatten_row(self, filled_row):
    return sum(filled_row, [])

  def __append_row_with_newline(self, flattened_row):
    return ['\n' if x==None else x for x in flattened_row]

  def __add_horizontal_fillers_if_between_rows(self, index, formatted_rows, number_of_rows):
    if index != number_of_rows - 1:
      formatted_rows = self.__add_horizontal_fillers(formatted_rows, number_of_rows)
    return formatted_rows

  def __add_horizontal_fillers(self, formatted_rows, number_of_rows):
    formatted_rows.append('===' + ('+===' * (number_of_rows - 1)))
    formatted_rows.append(['\n'])
    return formatted_rows

  def __convert_board_list_to_string(self, formatted_rows):
     return ''.join([item for sublist in formatted_rows for item in sublist])
