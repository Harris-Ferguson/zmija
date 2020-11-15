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
        safe_moves = [x for x in moves if not self.will_hit_hazard(current_location, x) and not self.head_collision_chance(current_location, x)]
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
        print("Good Moves ", good_moves)
        for move in good_moves:
          if self.trap_lookahead(self.game.get_self_head(), move, 3):
            print("lookahead removed: ", move)
            good_moves.remove(move)
        print("Pruned good moves", good_moves)
        if len(good_moves) == 0:
            try:
              return random.choice(safe_moves)
            except IndexError:
              return random.choice([x for x in moves if not self.will_hit_hazard(x) and not self.trap_lookahead(self.game.get_self_head(), x, 3)])
        else:
            return random.choice(good_moves)
