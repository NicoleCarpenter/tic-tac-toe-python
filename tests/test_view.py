import unittest
from lib.mock_io import MockIO
from lib.ttt_move_validator import TTTMoveValidator
from lib.selection_validator import SelectionValidator
from lib.input_validator import InputValidator
from lib.view import View

class TestView(unittest.TestCase):

  def setUp(self):
    self.io = MockIO()
    self.move_validator = TTTMoveValidator()
    self.selection_validator = SelectionValidator()
    self.input_validator = InputValidator()
    self.view = View(self.io, self.move_validator, self.selection_validator, self.input_validator)

  def tearDown(self):
    del self.io

  def test_io(self):
    self.assertEquals(self.view.io, self.io)

  def test_move_validator(self):
    self.assertEquals(self.view.move_validator, self.move_validator)

  def test_selection_validator(self):
    self.assertEquals(self.view.selection_validator, self.selection_validator)

  def test_input_validator(self):
    self.assertEquals(self.view.input_validator, self.input_validator)

  def test_prompt_play_mode(self):
    options = ['option1', 'option2']
    self.view.prompt_play_mode(options)
    self.assertEquals(self.io.display_called, True)
    self.assertEquals(self.io.display_called_with, options[-1])

  def test_get_play_mode(self):
    self.io.stub_user_input('1')
    options = ['1', '2']
    self.assertEquals(self.view.get_play_mode(options), '1')
    self.assertEquals(self.io.get_user_input_called, True)
    self.assertEquals(self.io.get_user_input_called_with, (''))

  def test_get_player_name(self):
    order = 'First'
    self.io.stub_user_input('John Doe')
    self.assertEquals(self.view.get_player_name(order), 'John Doe')
    self.assertEquals(self.io.get_user_input_called, True)
    self.assertEquals(self.io.get_user_input_called_with, 'First player, what is your name?')

  def test_display_player_order(self):
    player_name = 'Player 1'
    self.view.display_player_order(player_name)
    self.assertEquals(self.io.display_called, True)
    self.assertEquals(self.io.display_called_with, '\nPlayer 1 will go first')
    self.assertEquals(self.io.display_with_sleep_called, True)
    self.assertEquals(self.io.sleep_called, True)

  def test_prompt_player_move(self):
    player_name = 'Player 1'
    self.view.prompt_player_move(player_name)
    self.assertEquals(self.io.display_called, True)
    self.assertEquals(self.io.display_called_with, 'Player 1, select a position for your move: ')

  def test_get_player_move(self):
    self.io.stub_user_input('2')
    active_board = ['  '] * 9
    board_size = 9
    self.assertEquals(self.view.get_player_move(board_size, active_board), '2')
    self.assertEquals(self.io.get_user_input_called, True)
    self.assertEquals(self.io.get_user_input_called_with, '')

  def test_print_board(self):
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    self.view.print_board(board)
    self.assertEquals(self.io.display_called, True)
    self.assertEquals(self.io.display_called_with, board)

  def test_display_computer_thinking(self):
    self.view.display_computer_thinking()
    self.assertEquals(self.io.display_called, True)
    self.assertEquals(self.io.display_called_with, '\nThe computer is thinking')
    self.assertEquals(self.io.display_with_sleep_called, True)
    self.assertEquals(self.io.sleep_called, True)

  def test_display_tie_message(self):
    self.view.display_tie_message()
    self.assertEquals(self.io.display_called, True)
    self.assertEquals(self.io.display_called_with, 'Game over. It\'s a tie.')

  def test_display_winning_message(self):
    wining_player_name = 'Player 1'
    self.view.display_winning_message(wining_player_name)
    self.assertEquals(self.io.display_called, True)
    self.assertEquals(self.io.display_called_with, 'Game over. Player 1 wins!')

  def test_clear_screen(self):
    self.view.clear_screen()
    self.assertEquals(self.io.clear_called, True)  

  def test_loading(self):
    self.view.loading(3, '. ')
    self.assertEquals(self.io.display_with_sleep_called, True)
    self.assertEquals(self.io.display_with_sleep_called_with, '. ')
    self.assertEquals(self.io.sleep_called, True)