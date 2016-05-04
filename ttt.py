from source.io import IO
from source.view import View
from source.player_builder import PlayerBuilder
from source.ttt_setup import TTTSetup

if __name__ == '__main__':
  io = IO()
  view = View(io)
  player_builder = PlayerBuilder()
  tttsetup = TTTSetup(view, player_builder)

  play_mode = tttsetup.assign_play_mode()
  tttsetup.assign_player_names(play_mode)
