from lib.io import IO
from lib.view import View
from lib.human_move_generator import HumanMoveGenerator
from lib.computer_move_generator import ComputerMoveGenerator
from lib.player_builder import PlayerBuilder
from lib.ttt_setup import TTTSetup
from lib.ttt_game import TTTGame
from lib.ttt_board import TTTBoard

if __name__ == '__main__':
  io = IO()
  view = View(io)
  human_move_generator = HumanMoveGenerator(view)
  computer_move_generator = ComputerMoveGenerator()
  player_builder = PlayerBuilder(human_move_generator, computer_move_generator)
  tttsetup = TTTSetup(view, player_builder)

  tttboard = TTTBoard()

  play_mode = tttsetup.assign_play_mode()
  players = tttsetup.assign_player_names(play_mode)

  game = TTTGame(view, tttboard, players)
  game.play_game()
