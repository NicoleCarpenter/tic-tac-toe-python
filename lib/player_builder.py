from lib.human_player import HumanPlayer
from lib.computer_player import ComputerPlayer

class PlayerBuilder(object):

  def __init__(self, human_move_generator, computer_move_generator):
    self.human_move_generator = human_move_generator
    self.computer_move_generator = computer_move_generator

  def build_human_player(self, name, marker):
    return HumanPlayer(name, marker, self.human_move_generator)

  def build_computer_player(self, name, marker):
    return ComputerPlayer(name, marker, self.computer_move_generator)