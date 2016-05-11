import unittest
from lib.mock_io import MockIO
from lib.ttt_move_validator import TTTMoveValidator
from lib.selection_validator import SelectionValidator
from lib.view import View

class TestView(unittest.TestCase):

  def setUp(self):
    self.io = MockIO()
    move_validator = TTTMoveValidator()
    selection_validator = SelectionValidator()
    self.view = View(self.io, move_validator, selection_validator)

  def test_prompt_play_mode(self):
    self.view.prompt_play_mode(['option1', 'option2'])
    self.assertEquals(self.io.display_called, True)
    self.assertEquals(self.io.output_stream, 'option2')

  def test_get_play_mode(self):
    self.io.stubbed_user_input = '1'
    options = ['1', '2']
    self.assertEquals(self.view.get_play_mode(options), '1')
    self.assertEquals(self.io.get_user_input_called, True)

  def test_get_player_name(self):
    order = 'First'
    self.io.stubbed_user_input = 'John Doe'
    self.assertEquals(self.view.get_player_name(order), 'John Doe')
    self.assertEquals(self.io.get_user_input_called, True)
    self.assertEquals(self.io.output_stream, 'First player, what is your name?')

  def test_display_player_order(self):
    player_name = 'Player 1'
    self.view.display_player_order(player_name)
    self.assertEquals(self.io.display_called, True)
    self.assertEquals(self.io.output_stream, 'A coin has been flipped to determine order. Player 1 will go first.')

  def test_prompt_player_move(self):
    player_name = 'Player 1'
    self.view.prompt_player_move(player_name)
    self.assertEquals(self.io.display_called, True)
    self.assertEquals(self.io.output_stream, 'Player 1, select a position for your move: ')

  def test_get_player_move(self):
    self.io.stubbed_user_input = '2'
    active_board = ['  '] * 9
    board_size = 9
    self.assertEquals(self.view.get_player_move(board_size, active_board), '2')
    self.assertEquals(self.io.get_user_input_called, True)

  def test_print_board(self):
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    self.view.print_board(board)
    self.assertEquals(self.io.display_called, True)
    self.assertEquals(self.io.output_stream, board)

  def test_display_tie_message(self):
    self.view.display_tie_message()
    self.assertEquals(self.io.display_called, True)
    self.assertEquals(self.io.output_stream, 'Game over. It\'s a tie.')

  def test_display_winning_message(self):
    wining_player_name = 'Player 1'
    self.view.display_winning_message(wining_player_name)
    self.assertEquals(self.io.display_called, True)
    self.assertEquals(self.io.output_stream, 'Game over. Player 1 wins!')