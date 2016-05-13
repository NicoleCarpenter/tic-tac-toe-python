import abc

class Validator(object):

  def __init__(self):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def is_valid(self):
        pass