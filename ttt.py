from source.io import IO
from source.view import View
from source.ttt_setup import TTTSetup

if __name__ == '__main__':
  io = IO()
  view = View(io)
  tttsetup = TTTSetup(view)

  tttsetup.assign_play_mode()
