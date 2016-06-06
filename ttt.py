from lib.system_io import IO
from lib.validators.move_validator import TTTMoveValidator
from lib.validators.selection_validator import SelectionValidator
from lib.validators.input_validator import InputValidator
from lib.view.view import View
from lib.move_generators.human_move_generator import HumanMoveGenerator
from lib.move_generatprs.computer_move_generator import ComputerMoveGenerator
from lib.players.player_builder import PlayerBuilder
from lib.ttt.ttt_setup import TTTSetup
from lib.ttt.ttt_game import TTTGame
from lib.ttt.ttt_board import TTTBoard

if __name__ == '__main__':
  io = IO()
  move_validator = TTTMoveValidator()
  input_validator = InputValidator()
  selection_validator = SelectionValidator()
  view = View(io, move_validator, selection_validator, input_validator)
  
  human_move_generator = HumanMoveGenerator(view)
  computer_move_generator = ComputerMoveGenerator(view)
  player_builder = PlayerBuilder(human_move_generator, computer_move_generator)
  
  tttsetup = TTTSetup(view, player_builder)

  board_size = 9
  tttboard = TTTBoard(board_size)

  players = tttsetup.setup_game_players()

  game = TTTGame(view, tttboard, players)
  game.play_game()