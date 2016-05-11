class TTTSetup(object):

  def __init__(self, view, player_builder):
    self.view = view
    self.player_builder = player_builder

  def assign_play_mode(self):
    self.view.prompt_play_mode()
    return self.view.get_play_mode()

  def assign_player_names(self, play_mode):
    players = [self.player_builder.build_human_player(self.view.get_player_name())]
    if play_mode == '1':
      players.append(self.player_builder.build_human_player(self.view.get_player_name()))
    else:
      players.append(self.player_builder.build_computer_player('Computer'))
    return players
