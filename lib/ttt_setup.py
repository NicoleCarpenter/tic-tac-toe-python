class TTTSetup(object):

  def __init__(self, view, player_builder):
    self.view = view
    self.player_builder = player_builder

  def assign_play_mode(self):
    options = ['1 - Player vs Player', '2 - Player vs Computer']
    self.view.prompt_play_mode(options)
    return self.view.get_play_mode(options)

  def assign_player_names(self, play_mode):
    players = [self.player_builder.build_human_player(self.view.get_player_name('First'), 'X')]
    if play_mode == '1':
      players.append(self.player_builder.build_human_player(self.view.get_player_name('Second'), 'O'))
    else:
      players.append(self.player_builder.build_computer_player('Computer', 'O'))
    return players