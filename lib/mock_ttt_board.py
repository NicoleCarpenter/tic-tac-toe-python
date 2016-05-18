import abc
from lib.board import Board

class MockTTTBoard(Board):

  def __init__(self, board_size):
    self.board_size = board_size
    self.active_board = []
    self.format_board_to_string_called = False
    self.format_board_to_string_return = ''
    self.find_printable_board_positions_called = False
    self.printable_board_positions_return = ''
    self.place_piece_called = False
    self.place_piece_called_with = ''
    self.is_winning_conditions_met_called = False
    self.is_winning_conditions_met_return = ''
    self.is_tie_condition_met_called = False
    self.is_tie_condition_met_return = ''
    self.find_open_spaces_called = False
    self.find_open_spaces_return = ''

  def format_board_to_string(self, board):
    self.format_board_to_string_called = True
    self.format_board_to_string_called_with = board
    return self.format_board_to_string_return

  def stub_format_board_to_string(self, formatted_board):
    self.format_board_to_string_return = formatted_board

  def find_printable_board_positions(self):
    self.find_printable_board_positions_called = True
    return self.printable_board_positions_return

  def stub_find_printable_board_positions_return(self, board_positions):
    self.printable_board_positions_return = board_positions

  def place_piece(self, marker, space):
    self.place_piece_called = True
    self.place_piece_called_with = [marker, space]

  def is_tie_condition_met(self):
    self.is_tie_condition_met_called = True
    return self.is_tie_condition_met_return

  def stub_is_tie_condition_met(self, tie):
    self.is_tie_condition_met_return = tie

  def is_winning_conditions_met(self):
    self.is_winning_conditions_met_called = True
    return self.is_winning_conditions_met_return

  def stub_is_winning_conditions_met(self, winner):
    self.is_winning_conditions_met_return = winner

  def find_open_spaces(self):
    self.find_open_spaces_called = True
    return self.find_open_spaces_return

  def stub_find_open_spaces_return(self, open_spaces):
    self.find_open_spaces_return = open_spaces

  def stub_active_board(self, board):
    self.active_board = board

  def find_winning_marker(self):
    pass