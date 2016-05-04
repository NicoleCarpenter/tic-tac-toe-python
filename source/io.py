import abc
from source.interactable import Interactable

class IO(Interactable):

  def get_user_input(self, prompt):
    return raw_input('{0} '.format(prompt))

  def display(self, output):
    print('{0}'.format(output))
