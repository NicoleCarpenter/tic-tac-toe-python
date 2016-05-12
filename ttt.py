from lib.io import IO
from lib.ttt_move_validator import TTTMoveValidator
from lib.selection_validator import SelectionValidator
from lib.view import View
from lib.human_move_generator import HumanMoveGenerator
from lib.computer_move_generator import ComputerMoveGenerator
from lib.player_builder import PlayerBuilder
from lib.ttt_setup import TTTSetup
from lib.ttt_game import TTTGame
from lib.ttt_board import TTTBoard

if __name__ == '__main__':
  io = IO()
  move_validator = TTTMoveValidator()
  selection_validator = SelectionValidator()
  view = View(io, move_validator, selection_validator)
  human_move_generator = HumanMoveGenerator(view)
  computer_move_generator = ComputerMoveGenerator(move_validator, view)
  player_builder = PlayerBuilder(human_move_generator, computer_move_generator)
  tttsetup = TTTSetup(view, player_builder)

  board_size = 9
  tttboard = TTTBoard(board_size)

  mode = tttsetup.assign_play_mode()
  unordered_players = tttsetup.create_anonymous_players(mode)
  ordered_players = tttsetup.assign_player_order(unordered_players)

  game = TTTGame(view, tttboard, ordered_players)
  game.play_game()