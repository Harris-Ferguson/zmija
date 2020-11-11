from pathfinder_abstract import PathfinderBase
import random

class SimplePath(PathfinderBase):
    def next_move(self):
        possible_moves = ["up", "down", "left", "right"]
        # try to move towards some food
        closest_food = self.game.find_food()
        # if theres no food move in a random direction
        if not closest_food:
            choice = random.choice(possible_moves)
        else:
            choice = self.simple_path(closest_food[0])
        # if its dangerous move in a random other direction
        while self.will_hit_hazard(choice):
            choice = random.choice(possible_moves)
        return choice

    def simple_path(self, target):
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
