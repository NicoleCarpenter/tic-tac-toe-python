import abc
from lib.interactable import Interactable

class MockIO(Interactable):

  def __init__(self):
    self.get_user_input_called = False
    self.get_user_input_called_with = ''
    self.stubbed_user_input = ''
    self.display_called = False
    self.display_called_with = ''
    self.sleep_called = False
    self.sleep_called_with = ''
    self.display_with_sleep_called = False
    self.display_with_sleep_called_with = ''
    self.clear_called = False

  def get_user_input(self, prompt=''):
    self.get_user_input_called = True
    self.get_user_input_called_with = prompt
    return self.stubbed_user_input

  def stub_user_input(self, stubbed_input):
    self.stubbed_user_input = stubbed_input

  def display(self, output):
    self.display_called = True
    self.display_called_with = output

  def display_with_sleep(self, delay_time, output):
    self.display_with_sleep_called = True
    self.sleep_called = True
    self.display_with_sleep_called_with = output

  def clear(self):
    self.clear_called = True
