import unittest
import copy
from tests.mocks.mock_view import MockView
from lib.ttt.ttt_board import TTTBoard
from lib.computer_move_generator import ComputerMoveGenerator

class TestComputerMoveGenerator(unittest.TestCase):

  def setUp(self):
    self.view = MockView()
    self.move_generator = ComputerMoveGenerator(self.view)
    self.board = TTTBoard(9)

  def test_select_space_tie(self): 
    self.board.active_board = ['X','O','O','X','X','O','O','X','  ']
    move = self.move_generator.select_space(self.board, 'X')
    self.assertEquals(move, 9)
    self.assertEquals(self.view.display_computer_thinking_called, True)
    self.assertTrue(move >= 1, move <= 9)

  def test_select_space_block(self):
    self.board.active_board = ['O','O','  ','  ','X','  ','  ','  ','  ']
    move = self.move_generator.select_space(self.board, 'X')
    self.assertEquals(move, 3)
    self.assertEquals(self.view.display_computer_thinking_called, True)
    self.assertTrue(move >= 1, move <= 9)
  
  def test_select_space_win(self):
    self.board.active_board = ['X','X','  ','  ','O','  ','  ','O','  ']
    move = self.move_generator.select_space(self.board, 'X')
    self.assertEquals(move, 3)
    self.assertEquals(self.view.display_computer_thinking_called, True)
    self.assertTrue(move >= 1, move <= 9)

  @unittest.skip('long test run time')
  def test_select_space_unbeatable_first_move(self):
    self.play_all_games(self.board, 'O')

  @unittest.skip('long test run time')
  def test_select_space_unbeatable_second_move(self):
    self.play_all_games(self.board, 'X')

  def play_all_games(self, board, player_marker):
    if board.is_winning_conditions_met():
      self.assertNotEqual(board.find_winning_marker(), 'X')
    if not board.is_winning_conditions_met() and not board.is_tie_condition_met():
      if player_marker == 'X':
        for space in board.find_open_spaces():
          temp_board = copy.deepcopy(board)
          temp_board.place_piece('X', space + 1)
          self.play_all_games(temp_board, 'O')
      elif player_marker == 'O':
        temp_board = copy.deepcopy(board)
        temp_board.place_piece('O', self.move_generator.select_space(temp_board, 'O'))
        self.play_all_games(temp_board, 'X')