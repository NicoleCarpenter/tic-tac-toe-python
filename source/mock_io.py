import abc
from source.interactable import Interactable

class MockIO(Interactable):

  def __init__(self):
    self.get_user_input_called = False
    self.display_called = False
    self.stubbed_user_input = ''
    self.output_stream = ''

  def get_user_input(self, prompt):
    self.get_user_input_called = True
    return self.stubbed_user_input

  def display(self, output):
    self.display_called = True
    self.output_stream = output
