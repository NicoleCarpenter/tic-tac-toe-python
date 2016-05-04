import abc

class Interactable(object):
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def get_user_input(self, prompt):
    pass

  @abc.abstractmethod
  def display(self, output):
    pass
