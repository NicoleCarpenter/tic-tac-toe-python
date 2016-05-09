import abc
from lib.viewable import Viewable

class MockView(Viewable):

  def __init__(self):
    self.prompt_play_mode_called = False
    self.prompt_play_mode_called_with = ''
    self.get_play_mode_called = False
    self.get_play_mode_called_with = ''
    self.play_mode_return = ''
    self.get_player_name_called = False
    self.get_player_name_called_with = ''
    self.player_name_return = ''
    self.get_player_move_called = False
    self.get_player_move_called_with = ''
    self.player_move_return = ''
    self.print_board_called = False
    self.print_board_called_with = ''
    self.display_tie_message_called = False
    self.display_winning_message_called = False
    self.display_winning_message_called_with = ''

  def prompt_play_mode(self, options):
    self.prompt_play_mode_called = True
    self.prompt_play_mode_called_with = options

  def get_play_mode(self, options):
    self.get_play_mode_called = True
    self.get_play_mode_called_with = options
    return self.play_mode_return

  def stub_get_play_mode(self, play_mode_return):
    self.play_mode_return = play_mode_return

  def get_player_name(self, order):
    self.get_player_name_called = True
    self.get_player_name_called_with = order
    return self.player_name_return

  def stub_get_player_name(self, player_name_return):
    self.player_name_return = player_name_return

  def get_player_move(self, board_size, active_board):
    self.get_player_move_called = True
    self.get_player_move_called_with = [board_size, active_board]
    return self.player_move_return

  def stub_get_player_move(self, player_move_return):
    self.player_move_return = player_move_return

  def print_board(self, board):
    self.print_board_called = True
    self.print_board_called_with = board

  def display_tie_message(self):
    self.display_tie_message_called = True

  def display_winning_message(self, winning_player_name):
    self.display_winning_message_called = True
    self.display_winning_message_called_with = winning_player_name