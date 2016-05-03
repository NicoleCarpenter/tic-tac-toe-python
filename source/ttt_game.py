class TTTGame(object):

  def __init__(self, view, board):
    self.view = view
    self.board = board

  def play_game(self):
    move = self.view.get_player_move(self.board.board_size)
    self.board.place_piece('X', int(move), self.board.active_board)
    self.view.print_board(self.board.format_board_to_string(self.board.active_board))
