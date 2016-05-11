import abc

class Viewable(object):
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def prompt_play_mode(self, options):
    pass

  @abc.abstractmethod
  def get_play_mode(self, options):
    pass

  @abc.abstractmethod
  def get_player_name(self, order):
    pass

  @abc.abstractmethod
  def get_player_move(self, board_size, active_board):
    pass

  @abc.abstractmethod
  def print_board(self, board):
    pass

  @abc.abstractmethod
  def display_tie_message(self):
    pass

  @abc.abstractmethod
  def display_winning_message(self, winning_player_name):
    pass