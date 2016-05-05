import abc
from source.viewable import Viewable

class View(object):

  def __init__(self, io):
    self.io = io

  def prompt_play_mode(self):
    self.io.display('Please select your method of play:')
    self.io.display('1 - Player vs Player')
    self.io.display('2 - Player vs Computer')

  def get_play_mode(self):
    user_input = self.io.get_user_input('')
    while (not self.__is_valid_number(user_input)):
      self.io.display('Invalid selection')
      user_input = self.io.get_user_input('')
    return user_input

  def get_player_name(self):
    self.io.get_user_input('Player, what is your name?')

  def get_player_move(self, board_size):
    move = self.io.get_user_input('Select a position for your move')
    while (not self.__is_valid_number(move) or int(move) > board_size):
      self.io.display('Invalid move')
      move = self.io.get_user_input('')
    return move

  def print_board(self, board):
    self.io.display(board)

  def __is_valid_number(self, input):
    empty_string = ''
    return not empty_string and input.isdigit()
