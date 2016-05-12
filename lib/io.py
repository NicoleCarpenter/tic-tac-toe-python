import os
import time
import sys
import abc
from lib.interactable import Interactable

class IO(Interactable):

  def get_user_input(self, prompt):
    return raw_input('{0} '.format(prompt))

  def display(self, output):
    print('{0}'.format(output))

  def sleep(self, seconds=1):
    time.sleep(seconds)

  def display_with_sleep(self, seconds_to_pause, output):
    self.sleep(seconds_to_pause)
    sys.stdout.write(output)
    sys.stdout.flush()

  def clear(self):
    os.system('cls' if os.name == 'nt' else 'clear')