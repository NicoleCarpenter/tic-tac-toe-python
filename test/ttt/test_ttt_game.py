import unittest
import config
from test.mocks.mock_view import MockView
from test.mocks.mock_ttt_board import MockTTTBoard
from test.mocks.mock_move_generator import MockMoveGenerator
from lib.player import Player
from lib.ttt.ttt_game import TTTGame

xxx = config.OPEN_SPACE

class TestTTTGame(unittest.TestCase):

  def setUp(self):
    self.view = MockView()
    self.board_size = 9
    self.board = MockTTTBoard(self.board_size)
    self.move_generator = MockMoveGenerator()
    self.players = [Player('Player 1', 'X', self.move_generator),
                    Player('Player 2', 'O', self.move_generator)]
    self.game = TTTGame(self.view, self.board, self.players)

  def tearDown(self):
    del self.game

  def test_play_game_tie(self):
    self.board.active_board = \
    [ xxx, 'O', 'X',
      'X', 'O', 'X',
      'O', 'X', 'O']
    self.board.stub_board_positions([1,2,3,4,5,6,7,8,9])
    self.board.stub_is_tie_condition_met(True)
    self.players[0].move_generator.stub_select_space_return('1')
    self.game.play_game()

    self.assertEquals(self.view.print_board_called, True)
    self.assertEquals(self.view.prompt_player_move_called, True)
    self.assertEquals(self.view.prompt_player_move_called_with, 'Player 1')
    self.assertEquals(self.move_generator.select_space_called, True)
    self.assertEquals(self.board.place_piece_called, True)
    self.assertEquals(self.board.place_piece_called_with, ['X', 1])
    self.assertEquals(self.board.is_tie_condition_met_called, True)
    self.assertEquals(self.board.is_tie_condition_met_return, True)
    self.assertEquals(self.view.display_tie_message_called, True)
    self.assertEquals(self.view.display_winning_message_called, False)
    self.assertEquals(self.view.display_winning_message_called_with, '')
    self.assertEquals(self.game.game_over, True)
    self.assertEquals(self.game.winner, None)
    self.assertEquals(self.view.clear_screen_called, True)

  def test_play_game_win(self):
    self.board.stub_find_winning_marker('X')
    self.players[0].move_generator.stub_select_space_return('1')
    self.game.play_game()

    self.assertEquals(self.view.print_board_called, True)
    self.assertEquals(self.view.prompt_player_move_called, True)
    self.assertEquals(self.view.prompt_player_move_called_with, 'Player 1')
    self.assertEquals(self.move_generator.select_space_called, True)
    self.assertEquals(self.board.place_piece_called, True)
    self.assertEquals(self.board.place_piece_called_with, ['X', 1])
    self.assertEquals(self.board.is_tie_condition_met_called, True)
    self.assertEquals(self.board.is_tie_condition_met_return, False)
    self.assertEquals(self.view.display_tie_message_called, False)
    self.assertEquals(self.view.display_winning_message_called, True)
    self.assertEquals(self.view.display_winning_message_called_with, 'Player 1')
    self.assertEquals(self.game.game_over, True)
    self.assertEquals(self.game.winner, self.players[0])
    self.assertEquals(self.view.clear_screen_called, True)
