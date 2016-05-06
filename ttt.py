from source.io import IO
from source.view import View
from source.human_move_generator import HumanMoveGenerator
from source.computer_move_generator import ComputerMoveGenerator
from source.player_builder import PlayerBuilder
from source.ttt_setup import TTTSetup
from source.ttt_game import TTTGame
from source.ttt_board import TTTBoard

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
