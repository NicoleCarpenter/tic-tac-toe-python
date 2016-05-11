class TTTGame(object):

  def __init__(self, view, board, players):
    self.view = view
    self.board = board
    self.players = players
    self.board_positions = self.board.format_board_to_string(self.board.find_printable_board_positions())
    self.game_over = False
    self.winner = False

  def play_game(self):
    while not self.game_over:
      self.__alternate_player_turns()
    self.__display_results()

  def __alternate_player_turns(self):
    for player in self.players:
      if self.game_over: break
      self.__player_turn(player)

  def __player_turn(self, player):
    self.view.print_board(self.board_positions)
    self.view.prompt_player_move(player.name)
    move = player.move_generator.select_space(self.board.board_size, self.board.active_board)
    self.board.place_piece(player.marker, int(move))
    self.view.print_board(self.board.format_board_to_string(self.board.active_board))
    self.__is_winner(player)
    self.__is_tie()

  def __is_winner(self, player):
    if self.board.winning_conditions_met(player):
      self.winner = player
      self.game_over = True

  def __is_tie(self):
    if not '  ' in self.board.active_board:
      self.game_over = True

  def __display_results(self):
    if self.winner:
      self.view.display_winning_message(self.winner.name)
    else:
      self.view.display_tie_message()