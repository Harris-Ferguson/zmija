from pathfinder_abstract import PathfinderBase

class BoardSimulate(object):
    def __init__(self, board):
        self.board = board
        self.last_board = self.board

    def try_move(self, player, move):
        next_move = PathfinderBase.simulate_move(player["body"][0], move)
        self.last_board = self.board
        for snake in self.board["snakes"]:
            if snake["name"] == player["name"]:
                snake["body"].insert(0, next_move)

    def undo_move(self):
        self.board = self.last_board