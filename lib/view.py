import abc
from lib.viewable import Viewable

class View(Viewable):

  def __init__(self, io, move_validator, selection_validator, string_validator, board_presenter):
    self.io = io
    self.move_validator = move_validator
    self.selection_validator = selection_validator
    self.string_validator = string_validator
    self.board_presenter = board_presenter

  def prompt_numbered_options(self, options, prompt='Please make a selection'):
    self.io.display(prompt)
    for option in options:
      self.io.display(option)

  def get_numbered_option_selection(self, options):
    user_input = self.io.get_user_input()
    while not self.selection_validator.is_valid(user_input, options):
      self.io.display('Invalid selection')
      user_input = self.io.get_user_input('Select a numbered option from 1 to {0}: '.format(len(options)))
    return user_input

  def get_player_name(self, order):
    name = self.io.get_user_input('\n{0} player, what is your name?'.format(order))
    while not self.string_validator.is_valid(name):
      self.io.display('Name cannot be blank')
      name = self.io.get_user_input('What is your name?')
    return name

  def display_coin_flip(self):
    self.io.display('\nFlipping a coin to determine order ')
    self.loading(3, ' . ')

  def display_player_order(self, player_name):
    self.io.display('\n{0} will go first'.format(player_name))
    self.loading(2)

  def prompt_player_move(self, player_name):
    self.io.display('{0}, select a position for your move: '.format(player_name))

  def get_player_move(self, board):
    move = self.io.get_user_input()
    while not self.move_validator.is_valid(move, board):
      self.io.display('Invalid move')
      move = self.io.get_user_input('Select an open space from 1 to {0}: '.format(board.board_size))
    return move

  def print_board(self, board):
    if all(isinstance(item, int) for item in board):
      formatted_board_positions = self.board_presenter.find_printable_board_positions(board)
      self.io.display(self.board_presenter.format_board_to_string(formatted_board_positions)) 
    else:
      self.io.display(self.board_presenter.format_board_to_string(board))

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