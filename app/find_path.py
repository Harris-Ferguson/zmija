from pathfinder_abstract import PathfinderBase
import random


class FindPath(PathfinderBase):
    def next_move(self, target):
        move = self.find_path(target)
        return move

    def find_path(self, target):
        current_location = self.game.get_self_head()
        choices = []
        moves = ["left", "right", "down", "up"]
        safe_moves = [x for x in moves if not self.will_hit_hazard(x, current_location)
                      and not self.head_collision_chance(x)]
        if target["x"] != current_location["x"]:
            if target["x"] < current_location["x"]:
                choices.append("left")
            else:
                choices.append("right")
        if target["y"] != current_location["y"]:
            if target["y"] < current_location["y"]:
                choices.append("down")
            else:
                choices.append("up")
        good_moves = list(set(safe_moves).intersection(choices))
        if len(good_moves) == 1:
            return good_moves[0]
        if len(good_moves) == 0:
            return random.choice(safe_moves)
        else:
            return random.choice(good_moves)
