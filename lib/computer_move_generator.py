import abc
import copy
import config
from lib.move_generator import MoveGenerator
    
STARTING_DEPTH = 0
MAX_DEPTH = 7
TIE_SCORE = 0
WINNING_SCORE = -10

class ComputerMoveGenerator(MoveGenerator):

  def __init__(self, view):
    self.view = view
    computer_marker = config.OPPONENT_MARKER
    opponent_marker = config.PLAYER_MARKER
    self.markers = {1: computer_marker, -1: opponent_marker}

  def select_space(self, board):
    self.view.display_computer_thinking()
    return self.__negamax(board, STARTING_DEPTH, 1, -float('inf'), float('inf'))

  def __negamax(self, board, depth, color, alpha, beta):
    negamax_scores = {}
    best_score = -float('inf')
    best_move = -1

    if self.__is_terminal_node(board):
      return self.__score(board, depth)

    for space in board.find_open_spaces():
      temp_board = copy.deepcopy(board)
      temp_board.place_piece(self.markers[color], space + 1)
      score = -self.__negamax(temp_board, depth + 1, -color, -beta, -alpha)

      if best_score < score:
        best_score = score
        best_move = space

      alpha = max(score, alpha)
      if alpha >= beta:
        break

    if self.__is_full_board_evaluated(depth):
      return best_move + 1
    else:
      return best_score

  def __is_terminal_node(self, board):
    return board.is_tie_condition_met() or board.find_winning_marker() != None

  def __score(self, board, depth):
    if self.__is_max_node_depth(depth):
      return TIE_SCORE
    elif board.find_winning_marker() != None:
      return WINNING_SCORE
    else:
      return TIE_SCORE

  def __is_max_node_depth(self, depth):
    return depth >= MAX_DEPTH

  def __is_full_board_evaluated(self, depth):
    return depth == STARTING_DEPTH
