import random

class TTTSetup(object):

  def __init__(self, view, player_builder):
    self.view = view
    self.player_builder = player_builder

  def setup_game_players(self):
    self.view.clear_screen()
    play_mode = self.__assign_play_mode()
    players = self.__create_players(play_mode)
    ordered_players = self.__assign_player_order(players)
    self.view.display_player_order(ordered_players[0].name)
    return ordered_players

  def __assign_play_mode(self):
    prompt = 'Please select your method of play'
    options = ['1 - Player vs Player', '2 - Player vs Computer']
    self.view.prompt_numbered_options(options, prompt)
    return self.view.get_numbered_option_selection(options)

  def __create_players(self, play_mode):
    players = []
    player_names = self.__assign_player_names(play_mode)
    markers = self.__assign_player_markers(player_names)
    player_attribute_sets = zip(player_names, markers)
    for attribute_set in player_attribute_sets:
      players.append(self.player_builder.build_player(attribute_set[0], attribute_set[1]))
    return players

  def __assign_player_names(self, play_mode):
    player_names = [self.view.get_player_name('First')]
    if play_mode == '1':
      player_names.append(self.view.get_player_name('Second'))
    else:
      player_names.append('Computer')
    return player_names

  def __assign_player_markers(self, players):
    player_selection = self.__get_player_marker_selection(players)
    return self.__assign_player_markers_by_selection(player_selection)

  def __get_player_marker_selection(self, players):
    prompt = '\n{0}, do you want to play with X or O?'.format(players[0])
    options = ['1 - X', '2 - O']
    self.view.prompt_numbered_options(options, prompt)
    return self.view.get_numbered_option_selection(options)

  def __assign_player_markers_by_selection(self, player_selection):
    markers = ['X', 'O']
    if player_selection == '1':
      return markers
    else:
      return markers[::-1]

  def __assign_player_order(self, players):
    selection_type = self.__get_player_selection_type()
    if selection_type == '1':
      player_selection = self.__get_player_order_selection(players)
      return self.__assign_player_order_by_selection(players, player_selection)
    else:
      return self.__assign_player_order_randomly(players)

  def __get_player_selection_type(self):
    prompt = '\nDo you want to select who goes first, or have a coin flip determine the order randomly?'
    options = ['1 - Select order', '2 - Randomly assigned order']
    self.view.prompt_numbered_options(options, prompt)
    return self.view.get_numbered_option_selection(options)
    
  def __get_player_order_selection(self, players):
    prompt = '\nPlease select which player will go first'
    options = ['1 - {0}'.format(players[0].name), '2 - {0}'.format(players[1].name)]
    self.view.prompt_numbered_options(options, prompt)
    return self.view.get_numbered_option_selection(options)

  def __assign_player_order_by_selection(self, players, player_selection):
    if player_selection == '1':
      return players
    else:
      return players[::-1]

  def __assign_player_order_randomly(self, players):
    random.shuffle(players)
    self.view.display_coin_flip()
    return players