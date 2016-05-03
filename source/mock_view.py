import abc
from source.viewable import Viewable

class MockView(Viewable):

  def __init__(self):
    self.prompt_play_mode_called = False
    self.get_play_mode_called = False
    self.play_mode_return = ''
    self.get_player_name_called = False
    self.player_name_return = ''
    self.get_player_move_called = False
    self.print_board_called = False
    self.player_move_return = ''

  def prompt_play_mode(self):
    self.prompt_play_mode_called = True

  def get_play_mode(self):
    self.get_play_mode_called = True
    return self.play_mode_return

  def stub_get_play_mode(self, play_mode_return):
    self.play_mode_return = play_mode_return

  def get_player_name(self):
    self.get_player_name_called = True
    return self.player_name_return

  def stub_get_player_name(self, player_name_return):
    self.player_name_return = player_name_return

  def get_player_move(self, board_size):
    self.get_player_move_called = True
    return self.player_move_return

  def stub_get_player_move(self, player_move_return):
    self.player_move_return = player_move_return

  def print_board(self, board):
    self.print_board_called = True
