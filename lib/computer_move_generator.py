import abc
import copy
import config
from lib.move_generator import MoveGenerator

class ComputerMoveGenerator(MoveGenerator):

  def __init__(self, view):
    self.view = view
    self.STARTING_DEPTH = 0
    self.MAX_DEPTH = 7
    self.TIE_SCORE = 0
    self.WINNING_SCORE = -10
    self.computer_marker = config.OPPONENT_MARKER
    self.opponent_marker = config.PLAYER_MARKER

  def select_space(self, board):
    self.view.display_computer_thinking()
    markers = {1: self.computer_marker, -1: self.opponent_marker}
    return self.__negamax(board, markers, self.STARTING_DEPTH, 1, -float('inf'), float('inf'))

  def __negamax(self, board, markers, depth, color, alpha, beta):
    negamax_scores = {}
    best_score = -float('inf')
    best_move = -1

    if board.is_tie_condition_met() or board.find_winning_marker() != None:
      return self.__score(board, depth)

    for space in board.find_open_spaces():
      temp_board = copy.deepcopy(board)
      temp_board.place_piece(markers[color], space + 1)
      score = -self.__negamax(temp_board, markers, depth + 1, -color, -beta, -alpha)

      if best_score < score:
        best_score = score
        best_move = space

      alpha = max(score, alpha)
      if alpha >= beta:
        break

    if not self.__is_full_board_evaluated(depth):
      return best_score
    else:
      return best_move + 1

  def __score(self, board, depth):
    if self.__is_max_node_depth(depth):
      return self.TIE_SCORE
    elif board.find_winning_marker() != None:
      return self.WINNING_SCORE
    else:
      return self.TIE_SCORE

  def __is_max_node_depth(self, depth):
    return depth >= self.MAX_DEPTH

  def __is_full_board_evaluated(self, depth):
    return depth == self.STARTING_DEPTH
