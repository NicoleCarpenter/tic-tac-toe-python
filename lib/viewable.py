import abc

class Viewable(object):
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def prompt_play_mode(self):
    pass

  @abc.abstractmethod
  def get_play_mode(self):
    pass
