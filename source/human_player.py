import abc
from source.player import Player

class HumanPlayer(Player):

  def __init__(self, name):
    self.name = name
