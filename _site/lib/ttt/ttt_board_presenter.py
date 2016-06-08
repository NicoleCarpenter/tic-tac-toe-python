import math
import itertools

class TTTBoardPresenter(object):

  def format_board_to_string(self, board):
    formatted_board = self.__add_leading_spaces(board)
    formatted_rows = []
    number_of_rows = self.__find_number_of_rows(board)
    rows = self.__separate_rows(formatted_board)

    for index, row in enumerate(rows):
      formatted_rows.append(self.__format_row(row, number_of_rows))
      self.__add_horizontal_fillers_if_between_rows(index, formatted_rows, number_of_rows)

    return self.__convert_board_list_to_string(formatted_rows)

  def find_printable_board_positions(self, board):
    return map('{:1}'.format, board)

  def __add_leading_spaces(self, board):
    return [' ' + x if x!='  ' else x for x in board]

  def __find_number_of_rows(self, board):
    return int(math.sqrt(len(board)))

  def __separate_rows(self, board):
    rows = self.__find_number_of_rows(board)
    separated_rows = []
    last = 0
    while last < len(board):
      separated_rows.append(board[last:last+rows])
      last += rows
    return separated_rows

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