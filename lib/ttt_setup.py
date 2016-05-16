import random

class TTTSetup(object):

  def __init__(self, view, player_builder):
    self.view = view
    self.player_builder = player_builder

  def setup_game_players(self):
    self.view.clear_screen()
    play_mode = self.__assign_play_mode()
    named_players = self.__assign_player_names(play_mode)
    ordered_and_named_players = self.__assign_player_order(named_players)
    self.view.display_player_order(ordered_and_named_players[0].name)
    return ordered_and_named_players

  def __assign_play_mode(self):
    prompt = 'Please select your method of play'
    options = ['1 - Player vs Player', '2 - Player vs Computer']
    self.view.prompt_numbered_options(options, prompt)
    return self.view.get_numbered_option_selection(options)

  def __assign_player_names(self, play_mode):
    players = [self.player_builder.build_human_player(self.view.get_player_name('First'), 'X')]
    if play_mode == '1':
      players.append(self.player_builder.build_human_player(self.view.get_player_name('Second'), 'O'))
    else:
      players.append(self.player_builder.build_computer_player('Computer', 'O'))
    return players

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
    prompt = 'Please select which player will go first'
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