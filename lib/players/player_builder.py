from lib.players.player import Player

class PlayerBuilder(object):

  def __init__(self, human_move_generator, computer_move_generator):
    self.human_move_generator = human_move_generator
    self.computer_move_generator = computer_move_generator

  def build_player(self, name, marker):
    if name != 'Computer':
      return Player(name, marker, self.human_move_generator)
    else: 
      return Player(name, marker, self.computer_move_generator)