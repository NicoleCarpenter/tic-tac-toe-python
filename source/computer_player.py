import abc
from source.player import Player

class ComputerPlayer(Player):

  def __init__(self, name):
    self.name = name
