import unittest
from source.mock_view import MockView
from source.ttt_board import TTTBoard
from source.ttt_game import TTTGame
from source.player_builder import PlayerBuilder

class TestTTTGame(unittest.TestCase):

  def setUp(self):
    view = MockView()
    board = TTTBoard()
    self.game = TTTGame(view, board)

  def tearDown(self):
    del self.game

  def test_play_game(self):
    self.game.view.stub_get_player_move('5')
    self.game.play_game()
    self.assertEquals(self.game.board.active_board[4], ' X')
    self.assertEquals(self.game.view.print_board_called, True)
