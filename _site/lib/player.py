class Player(object):

  def __init__(self, name, marker, move_generator):
    self.name = name
    self.marker = marker
    self.move_generator = move_generator