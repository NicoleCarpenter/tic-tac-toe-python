class TTTGame(object):

  def __init__(self, view, board, players):
    self.view = view
    self.board = board
    self.players = players
    self.game_over = False
    self.winner = False

  def play_game(self):
    self.view.clear_screen()
    while not self.game_over:
      self.__alternate_player_turns()
    self.__display_results()

  def __alternate_player_turns(self):
    for player in self.players:
      if self.game_over: break
      self.__player_turn(player)

  def __player_turn(self, player):
    self.view.print_board(self.board.board_positions)
    self.view.print_board(self.board.active_board)
    self.view.prompt_player_move(player.name)
    move = player.move_generator.select_space(self.board, player.marker)
    self.board.place_piece(player.marker, int(move))
    self.__is_winner(player)
    self.__is_tie()
    self.view.clear_screen()

  def __is_winner(self, player):
    if self.board.is_winning_conditions_met():
      self.winner = player
      self.game_over = True

  def __is_tie(self):
    if self.board.is_tie_condition_met():
      self.game_over = True

  def __display_results(self):
    self.view.print_board(self.board.board_positions)
    self.view.print_board(self.board.active_board)
    if self.winner:
      self.view.display_winning_message(self.winner.name)
    else:
      self.view.display_tie_message()