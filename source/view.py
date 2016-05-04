import abc
from source.viewable import Viewable
from source.io import IO

class View(object):

  def __init__(self, io):
    self.io = io

  def prompt_play_mode(self):
    self.io.display('Please select your method of play:')
    self.io.display('1 - Player vs Player')
    self.io.display('2 - Player vs Computer')

  def get_play_mode(self):
    user_input = self.io.get_user_input('')
    while (not self.__is_valid_selection(user_input)):
      self.io.display('Invalid selection')
      user_input = self.io.get_user_input('')
    return user_input

  def __is_valid_selection(self, input):
    empty_string = ''
    return not empty_string and input.isdigit()
