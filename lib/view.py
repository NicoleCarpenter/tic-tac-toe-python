import abc
from lib.viewable import Viewable

class View(Viewable):

  def __init__(self, io, move_validator, selection_validator):
    self.io = io
    self.move_validator = move_validator
    self.selection_validator = selection_validator

  def prompt_play_mode(self, options):
    self.io.display('\nPlease select your method of play:')
    for option in options:
      self.io.display(option)

  def get_play_mode(self, options):
    user_input = self.io.get_user_input('')
    while not self.selection_validator.is_valid(user_input, options):
      self.io.display('Invalid selection')
      user_input = self.io.get_user_input('Select a numbered option from 1 to {0}: '.format(len(options)))
    return user_input

  def get_player_name(self, order):
    return self.io.get_user_input('{0} player, what is your name?'.format(order))

  def display_player_order(self, player_name):
    self.io.display('Flipping a coin to determine order ')
    self.loading(3, ' . ')
    self.io.display('\n{0} will go first'.format(player_name))

  def prompt_player_move(self, player_name):
    self.io.display('{0}, select a position for your move: '.format(player_name))

  def get_player_move(self, board_size, active_board):
    move = self.io.get_user_input('')
    while not self.move_validator.is_valid(move, board_size, active_board):
      self.io.display('Invalid move')
      move = self.io.get_user_input('Select an open space from 1 to {0}: '.format(board_size))
    return move

  def print_board(self, board):
    self.io.display(board)

  def display_computer_thinking(self):
    self.io.display('\nThe computer is thinking')
    self.loading(3, ' . ')

  def display_tie_message(self):
    self.io.display('Game over. It\'s a tie.')

  def display_winning_message(self, winning_player_name):
    self.io.display('Game over. {0} wins!'.format(winning_player_name))

  def clear_screen(self):
    self.io.clear()

  def loading(self, seconds_to_pause, output_to_display=''):
    for second in range(0, seconds_to_pause):
      self.io.display_with_sleep(1, output_to_display)