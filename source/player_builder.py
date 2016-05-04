from source.human_player import HumanPlayer
from source.computer_player import ComputerPlayer

class PlayerBuilder(object):

  def build_human_player(self, name):
    return HumanPlayer(name)

  def build_computer_player(self, name):
    return ComputerPlayer(name)
