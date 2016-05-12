import abc

class Interactable(object):
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def get_user_input(self, prompt):
    pass

  @abc.abstractmethod
  def display(self, output):
    pass

  @abc.abstractmethod
  def sleep(self, seconds):
    pass

  @abc.abstractmethod
  def display_with_sleep(self):
    pass

  @abc.abstractmethod
  def clear(self):
    pass
