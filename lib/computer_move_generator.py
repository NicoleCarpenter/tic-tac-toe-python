import abc
import copy
from lib.move_generator import MoveGenerator

class ComputerMoveGenerator(MoveGenerator):

  def __init__(self, view):
    self.view = view
    
  def select_space(self, board, player_marker):
    current_player = player_marker
    opponent = self.__find_opponent_marker(player_marker)
    starting_depth = 0
    self.view.display_computer_thinking()
    return self.__negamax(board, current_player, opponent, starting_depth, {})

  def __negamax(self, board, player, opponent, depth, negamax_scores):
    max_depth = 7
    if depth >= max_depth:
      return 0
    if board.is_winning_conditions_met() or board.is_tie_condition_met():
      return self.__score(board)
        
    for space in board.find_open_spaces():
      temp_board = copy.deepcopy(board)
      temp_board.place_piece(player, space + 1)
      negamax_scores[space] = -1 * self.__negamax(temp_board, opponent, player, depth + 1, {})

    starting_depth = 0
    best_spot_index = max(negamax_scores, key=negamax_scores.get)
    highest_negamax_value = negamax_scores[best_spot_index]

    if depth != starting_depth:
      return highest_negamax_value
    else:
      return best_spot_index + 1

  def __score(self, board):
    if board.find_winning_marker() == None:
      return 0
    else:
      return -10

  def __find_opponent_marker(self, player):
    if player == 'X':
      return 'O'
    else:
      return 'X'