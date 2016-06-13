from lib.io import IO
from lib.move_validator import MoveValidator
from lib.selection_validator import SelectionValidator
from lib.string_validator import StringValidator
from lib.ttt.ttt_board_presenter import TTTBoardPresenter
from lib.view import View
from lib.human_move_generator import HumanMoveGenerator
from lib.computer_move_generator import ComputerMoveGenerator
from lib.player_builder import PlayerBuilder
from lib.ttt.ttt_setup import TTTSetup
from lib.ttt.ttt_game import TTTGame
from lib.ttt.ttt_board import TTTBoard

if __name__ == '__main__':
  io = IO()
  move_validator = MoveValidator()
  string_validator = StringValidator()
  selection_validator = SelectionValidator()
  ttt_board_presenter = TTTBoardPresenter()
  view = View(io, move_validator, selection_validator, string_validator, ttt_board_presenter)

  human_move_generator = HumanMoveGenerator(view)
  computer_move_generator = ComputerMoveGenerator(view)
  player_builder = PlayerBuilder(human_move_generator, computer_move_generator)

  tttsetup = TTTSetup(view, player_builder)

  board_size = 9
  tttboard = TTTBoard(board_size)

  players = tttsetup.setup_game_players()

  game = TTTGame(view, tttboard, players)
  game.play_game()
