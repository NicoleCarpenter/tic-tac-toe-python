import abc
from source.viewable import Viewable

class MockView(Viewable):

  def __init__(self):
    self.prompt_play_mode_called = False
    self.get_play_mode_called = False

  def prompt_play_mode(self):
    self.prompt_play_mode_called = True

  def get_play_mode(self):
    self.get_play_mode_called = True
