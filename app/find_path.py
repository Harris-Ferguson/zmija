from pathfinder_abstract import PathfinderBase
import random


class FindPath(PathfinderBase):
    def next_move(self, target):
        next_move = self.find_path(target)
        return next_move

    def find_path(self, target):
        current_location = self.game.get_self_head()
        choices = []
        safe_moves = self.filter_unsafe_moves(["left", "right", "down", "up"])
        if target["x"] != current_location["x"]:
            if target["x"] < current_location["x"]:
                choices.append("left")
            else:
                choices.append("right")
        if target["y"] != current_location["y"]:
            if target["y"] < current_location["y"]:
                choices.append("up")
            else:
                choices.append("down")
        choices = self.filter_unsafe_moves(choices)
        if len(choices) == 1:
            return choices[0]
        if len(choices) == 0:
            return random.choice(safe_moves)
        else:
            return random.choice(choices)

    def filter_unsafe_moves(self, moves):
        for move in moves:
            if self.will_hit_hazard(move):
                moves.remove(move)
        return moves
