class TTTGame(object):

  def __init__(self, view, board, players):
    self.view = view
    self.board = board
    self.players = players
    self.winner = self.board.find_winning_marker()
    self.game_over = self.__is_game_over()

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

    self.check_for_winner(player)
    self.game_over = self.__is_game_over()
    self.view.clear_screen()

  def __is_game_over(self):
    return self.__is_tie() or self.winner != None

  def check_for_winner(self, player):
    if self.board.find_winning_marker() != None:
      self.winner = player

  def __is_tie(self):
    return self.board.is_tie_condition_met()

  def __display_results(self):
    self.view.print_board(self.board.board_positions)
    self.view.print_board(self.board.active_board)
    if self.winner:
      self.view.display_winning_message(self.winner.name)
    else:
      self.view.display_tie_message()