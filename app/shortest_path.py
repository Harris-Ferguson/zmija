from pathfinder_abstract import PathfinderBase

class ShortestPath(PathfinderBase):
    def next_move(self):
        safe_squares = self.get_safe_squares()

    def get_safe_squares(self):
        bad_squares = self.game.find_bad_squares()
        print(bad_squares)
        board = []
        for x in range(self.game.get_board_size()["width"]):
            for y in range(self.game.get_board_size()["height"]):
                if {"x":x,"y":y} not in bad_squares:
                    print(x, y)
                    board.append({"x":x,"y":y})
        return board
