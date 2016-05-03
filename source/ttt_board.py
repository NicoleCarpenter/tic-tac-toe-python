import abc
import itertools
from source.board import Board

class TTTBoard(Board):

  def __init__(self):
    self.board_size = 9
    self.active_board = ['  '] * self.board_size

  def find_number_of_rows(self):
    return super(TTTBoard, self).find_number_of_rows()

  def separate_rows(self, board):
    return super(TTTBoard, self).separate_rows(board)

  def format_board_to_string(self, board):
    formatted_rows = []
    number_of_rows = self.find_number_of_rows()
    rows = self.separate_rows(board)
    for index, row in enumerate(rows):
      formatted_rows.append(self.__format_row(row, number_of_rows))
      self.__add_horizontal_fillers_if_between_rows(index, formatted_rows, number_of_rows)
    converted_string = self.__convert_board_list_to_string(formatted_rows)
    return converted_string

  def place_piece(self, marker, space, active_board):
    super(TTTBoard, self).place_piece(marker, space, active_board)

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
