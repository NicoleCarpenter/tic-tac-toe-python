class TTTGame(object):

  def __init__(self, view, board, players):
    self.view = view
    self.board = board
    self.players = players

  def play_game(self):
    move = self.__player_turn(self.players[0])
    self.board.place_piece('X', int(move), self.board.active_board)
    self.view.print_board(self.board.format_board_to_string(self.board.active_board))

    move = self.__player_turn(self.players[1])
    self.board.place_piece('O', int(move), self.board.active_board)
    self.view.print_board(self.board.format_board_to_string(self.board.active_board))

  def __player_turn(self, player):
    return player.move_generator.select_space(self.board.board_size)
