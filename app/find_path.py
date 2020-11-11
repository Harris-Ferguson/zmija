from pathfinder_abstract import PathfinderBase


class FindPath(PathfinderBase):
    def next_move(self, target):
        safe_squares = self.get_safe_squares()
        next_move = self.find_path(safe_squares, target)

    def get_safe_squares(self):
        bad_squares = self.game.find_bad_squares()
        print(bad_squares)
        board = []
        for x in range(self.game.get_board_size()["width"]):
            for y in range(self.game.get_board_size()["height"]):
                if {"x": x, "y": y} not in bad_squares:
                    print(x, y)
                    board.append({"x": x, "y": y})
        return board

    def find_path(self, safe_squares, target):
        current_location = self.game.get_self_head()
        if target["x"] != current_location["x"]:
            if target["x"] < current_location["x"]:
                return "left"
            else:
                return "right"
        elif target["y"] != current_location["y"]:
            if target["y"] < current_location["y"]:
                return "up"
            else:
                return "down"
