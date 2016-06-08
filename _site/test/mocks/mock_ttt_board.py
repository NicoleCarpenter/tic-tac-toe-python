import abc
from lib.board import Board

class MockTTTBoard(Board):

  def __init__(self, board_size):
    self.board_size = board_size
    self.active_board = []
    self.board_positions = []
    self.place_piece_called = False
    self.place_piece_called_with = ''
    self.find_open_spaces_called = False
    self.find_open_spaces_return = ''
    self.is_winning_conditions_met_called = False
    self.is_winning_conditions_met_return = ''
    self.is_tie_condition_met_called = False
    self.is_tie_condition_met_return = ''
    self.find_winning_marker_called = False
    self.find_winning_marker_return = ''

  def stub_active_board(self, board):
    self.active_board = board

  def stub_board_positions(self, board_positions):
    self.board_positions = board_positions

  def place_piece(self, marker, space):
    self.place_piece_called = True
    self.place_piece_called_with = [marker, space]

  def find_open_spaces(self):
    self.find_open_spaces_called = True
    return self.find_open_spaces_return

  def stub_find_open_spaces_return(self, open_spaces):
    self.find_open_spaces_return = open_spaces

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

  def find_winning_marker(self):
    self.find_winning_marker_called = True
    return self.find_winning_marker_return

  def stub_find_winning_marker(self, winner):
    self.find_winning_marker_return = winner