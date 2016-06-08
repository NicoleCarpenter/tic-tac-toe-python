import abc
import copy
import config
from lib.move_generator import MoveGenerator

class ComputerMoveGenerator(MoveGenerator):

  def __init__(self, view):
    self.view = view
    self.MAX_DEPTH = 7
    self.STARTING_DEPTH = 0
    
  def select_space(self, board, current_player_marker):
    opponent_marker = self.__find_opponent_marker(current_player_marker)
    self.view.display_computer_thinking()
    return self.__negamax(board, current_player_marker, opponent_marker, self.STARTING_DEPTH, {})

  def __negamax(self, board, player_marker, opponent_marker, depth, negamax_scores):
    if depth >= self.MAX_DEPTH:
      return 0
    if board.is_tie_condition_met() or board.find_winning_marker() != None:
      return self.__score(board)
        
    for space in board.find_open_spaces():
      temp_board = copy.deepcopy(board)
      temp_board.place_piece(player_marker, space + 1)
      negamax_scores[space] = -1 * self.__negamax(temp_board, opponent_marker, player_marker, depth + 1, {})

    best_spot_index = max(negamax_scores, key=negamax_scores.get)
    highest_negamax_value = negamax_scores[best_spot_index]

    if depth != self.STARTING_DEPTH:
      return highest_negamax_value
    else:
      return best_spot_index + 1

  def __score(self, board):
    if board.find_winning_marker() == None:
      return 0
    else:
      return -10

  def __find_opponent_marker(self, current_player_marker):
    if current_player_marker == config.PLAYER_MARKER:
      return config.OPPONENT_MARKER
    else:
      return config.PLAYER_MARKER