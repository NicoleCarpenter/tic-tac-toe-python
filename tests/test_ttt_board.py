import unittest
from lib.mock_move_generator import MockMoveGenerator
from lib.mock_player import MockPlayer
from lib.ttt_board import TTTBoard

class TestTTTBoard(unittest.TestCase):

  def setUp(self):
    board_size = 9
    self.board = TTTBoard(board_size)

  def tearDown(self):
    del self.board

  def test_format_to_board_string(self):
    empty_board = ['  '] * 9
    printed_board = self.board.format_board_to_string(empty_board)
    self.assertEquals(printed_board, '   |   |  \n===+===+===\n   |   |  \n===+===+===\n   |   |  \n')

    board_positions = [' 1',' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9']
    printed_board = self.board.format_board_to_string(board_positions)
    self.assertEquals(printed_board, ' 1 | 2 | 3\n===+===+===\n 4 | 5 | 6\n===+===+===\n 7 | 8 | 9\n')

  def test_find_printable_board_positions(self):
    board_positions = self.board.find_printable_board_positions()
    self.assertEquals(board_positions, [' 1',' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9'])

    board_size = 16
    self.board = TTTBoard(board_size)
    board_positions = self.board.find_printable_board_positions()
    self.assertEquals(board_positions, [' 1',' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9',' 10',' 11',' 12',' 13',' 14',' 15',' 16'])

  def test_place_piece(self):
    marker = 'X'
    self.board.place_piece(marker, 2)
    self.assertIn((' ' + marker), self.board.active_board)
    self.assertEqual(self.board.active_board[1], ' ' + marker)

  def test_find_winning_combinations(self):
    winning_combos = self.board.find_winning_combinations()
    self.assertEquals(winning_combos, [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]])

    board_size = 16
    self.board = TTTBoard(board_size)
    winning_combos = self.board.find_winning_combinations()
    self.assertEquals(winning_combos, [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,16],[1,6,11,16],[4,7,10,13]])
  
  def test_winning_conditions_met(self):
    generator = MockMoveGenerator()
    player = MockPlayer('Player 1', 'X', generator)
    
    self.board.active_board = [' X',' X',' X','  ','  ','  ','  ','  ','  ']
    winner = self.board.winning_conditions_met(player)
    self.assertEquals(winner, True)

    self.board.active_board = ['  ','  ','  ',' X',' X',' X','  ','  ','  ']
    winner = self.board.winning_conditions_met(player)
    self.assertEquals(winner, True)

    self.board.active_board = ['  ','  ','  ','  ','  ','  ',' X',' X',' X']
    winner = self.board.winning_conditions_met(player)
    self.assertEquals(winner, True)

    self.board.active_board = [' X','  ','  ',' X','  ','  ',' X','  ','  ']
    winner = self.board.winning_conditions_met(player)
    self.assertEquals(winner, True)

    self.board.active_board = ['  ',' X','  ','  ',' X','  ','  ',' X','  ']
    winner = self.board.winning_conditions_met(player)
    self.assertEquals(winner, True)

    self.board.active_board = ['  ','  ',' X','  ','  ',' X','  ','  ',' X']
    winner = self.board.winning_conditions_met(player)
    self.assertEquals(winner, True)

    self.board.active_board = [' X','  ','  ','  ',' X','  ','  ','  ',' X']
    winner = self.board.winning_conditions_met(player)
    self.assertEquals(winner, True)

    self.board.active_board = ['  ','  ',' X','  ',' X','  ',' X','  ','  ']
    winner = self.board.winning_conditions_met(player)
    self.assertEquals(winner, True)

    self.board.active_board = ['  ','  ','  ','  ','  ','  ','  ','  ','  ']
    winner = self.board.winning_conditions_met(player)
    self.assertEquals(winner, False)

    self.board.active_board = [' X',' O',' X','  ','  ','  ','  ','  ','  ']
    winner = self.board.winning_conditions_met(player)
    self.assertEquals(winner, False)

    self.board.active_board = [' O',' O',' O','  ','  ','  ','  ','  ','  ']
    winner = self.board.winning_conditions_met(player)
    self.assertEquals(winner, False)

