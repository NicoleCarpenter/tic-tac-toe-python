import abc

class Viewable(object):
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def prompt_numbered_options(self, options):
    pass

  @abc.abstractmethod
  def get_numbered_option_selection(self, options):
    pass

  @abc.abstractmethod
  def get_player_name(self, order):
    pass

  @abc.abstractmethod
  def display_coin_flip(self):
    pass

  @abc.abstractmethod
  def display_player_order(self, player_name):
    pass

  @abc.abstractmethod
  def prompt_player_move(self, player):
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

  @abc.abstractmethod
  def clear_screen(self):
    pass

  @abc.abstractmethod
  def loading(self):
    pass