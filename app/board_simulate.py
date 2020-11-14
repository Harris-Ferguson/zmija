from pathfinder_abstract import PathfinderBase

class BoardSimulate(object):
    def __init__(self, board):
        self.board = board
        self.last_board = self.board

    def try_move(self, player, move):
        next_move = PathfinderBase.simulate_move(player["body"][0], move)
        bad_squares = self.create_invalid_squares()
        for snake in self.board["snakes"]:
            if snake["name"] == player["name"]:
                snake["body"].insert(0, next_move)
                if next_move in bad_squares:
                    self.board["snakes"].remove(snake)
                for food in self.board["food"]:
                    if next_move == food:
                        self.board["food"].remove(food)

    def undo_move(self):
        self.board = self.last_board

    def create_invalid_squares(self):
        """
        creates a list of every square which causes death
        """
        bad_squares = []
        for snake in self.board["snakes"]:
            for spot in snake["body"]:
                # get every square that isn't a tail
                if spot != snake["body"][-1]:
                    bad_squares.append(spot)
        for x in range(0, self.board["width"] - 1):
            for y in range(0, self.board['height'] - 1):
                bad_squares.append({"x": x, "y": self.board["height"]})
                bad_squares.append({"x": x, "y": -1})
                bad_squares.append({"x": self.board["width"], "y": y})
                bad_squares.append({"x": -1, "y": y})
        return bad_squares