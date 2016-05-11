import unittest
from lib.mock_view import MockView
from lib.ttt_board import TTTBoard
from lib.ttt_game import TTTGame
from lib.human_move_generator import HumanMoveGenerator
from lib.human_player import HumanPlayer

class TestTTTGame(unittest.TestCase):

  def setUp(self):
    view = MockView()
    board = TTTBoard()
    move_generator = HumanMoveGenerator(view)
    players = [HumanPlayer('Jack', move_generator),
               HumanPlayer('Jill', move_generator)]
    self.game = TTTGame(view, board, players)

  def tearDown(self):
    del self.game

  def test_play_game(self):
    self.game.view.stub_get_player_move('5')
    self.game.play_game()
    self.assertEquals(self.game.board.active_board[4], ' O')
    self.assertEquals(self.game.view.print_board_called, True)
