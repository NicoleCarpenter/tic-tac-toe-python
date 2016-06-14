import unittest
import copy
import config
from test.mocks.mock_view import MockView
from lib.ttt.ttt_board import TTTBoard
from lib.computer_move_generator import ComputerMoveGenerator

xxx = config.OPEN_SPACE

class TestComputerMoveGenerator(unittest.TestCase):

  def setUp(self):
    self.view = MockView()
    self.move_generator = ComputerMoveGenerator(self.view)
    self.board = TTTBoard(9)

  def test_select_space_tie(self):
    self.board.active_board = \
    [ 'X', 'O', 'O',
      'X', 'X', 'O',
      'O', 'X', xxx ]
    move = self.move_generator.select_space(self.board)
    self.assertEquals(move, 9)
    self.assertEquals(self.view.display_computer_thinking_called, True)

  def test_select_space_block(self):
    self.board.active_board = \
    [ xxx, xxx, xxx,
      xxx, 'O', xxx,
      xxx, 'X', 'X' ]
    move = self.move_generator.select_space(self.board)
    self.assertEquals(move, 7)
    self.assertEquals(self.view.display_computer_thinking_called, True)

  def test_select_space_win(self):
    self.board.active_board = \
    [ 'O', 'O', xxx,
      xxx, xxx, xxx,
      xxx, 'X' ,'X' ]
    move = self.move_generator.select_space(self.board)
    self.assertEquals(move, 3)
    self.assertEquals(self.view.display_computer_thinking_called, True)

  def test_select_space_second_move_block(self):
    self.board.active_board = \
    [ 'X', xxx, xxx,
      xxx, 'O', xxx,
      xxx, xxx,' X' ]
    move = self.move_generator.select_space(self.board)
    self.assertNotEqual(move, 3)
    self.assertNotEqual(move, 7)
    self.assertNotEqual(move, 1)
    self.assertNotEqual(move, 9)
    self.assertNotEqual(move, 5)

  def test_select_space_center_fork(self):
    self.board.active_board = \
    [ 'O', 'O', 'X',
      'X', xxx, xxx,
      xxx, xxx, xxx]
    move = self.move_generator.select_space(self.board)
    self.assertEquals(move, 5)

  def test_select_space_center_fork(self):
    self.board.active_board = \
    [ 'X', 'X', 'O',
      xxx, xxx, xxx,
      xxx, xxx, xxx]
    move = self.move_generator.select_space(self.board)
    self.assertIn(move, [5, 6])

  def test_select_space_last_move_win(self):
    self.board.active_board = \
    [ 'X', 'O', 'X',
      'O', 'O', 'X',
      xxx, 'X', xxx ]
    move = self.move_generator.select_space(self.board)
    self.assertEquals(move, 9)

  def test_select_space_unbeatable_first_move(self):
    self.play_all_games(self.board, 'O', [])

  def test_select_space_unbeatable_second_move(self):
    self.play_all_games(self.board, 'X', [])

  def play_all_games(self, board, player_marker, player_moves):
    if board.find_winning_marker() != None:
      self.assertNotEqual(board.find_winning_marker(), 'X')
    if board.find_winning_marker() == None and not board.is_tie_condition_met():
      if player_marker == 'X':
        for space in board.find_open_spaces():
          temp_board = copy.deepcopy(board)
          temp_board.place_piece('X', space + 1)
          new_moves = copy.deepcopy(player_moves)
          new_moves.append(space)
          self.play_all_games(temp_board, 'O', new_moves)
      elif player_marker == 'O':
        temp_board = copy.deepcopy(board)
        temp_board.place_piece('O', self.move_generator.select_space(temp_board))
        self.play_all_games(temp_board, 'X', player_moves)
