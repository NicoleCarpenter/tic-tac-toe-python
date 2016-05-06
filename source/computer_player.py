import abc
import random
from source.player import Player

class ComputerPlayer(Player):

  def __init__(self, name, move_generator):
    self.name = name
    self.move_generator = move_generator