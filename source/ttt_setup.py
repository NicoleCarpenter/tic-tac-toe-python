from source.view import View

class TTTSetup(object):

  def __init__(self, view):
    self.view = view

  def assign_play_mode(self):
    self.view.prompt_play_mode()
    return self.view.get_play_mode()
