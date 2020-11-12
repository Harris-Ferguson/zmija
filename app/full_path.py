from pathfinder_abstract import PathfinderBase
import random

class FullPath(PathfinderBase):
    def next_move(self, target):
        possible_moves = ["up", "down", "left", "right"]
        prefered_moves = []
        food = self.game.find_food()
        choice = random.choice(possible_moves)

        'Avoid any food'
        for x in possible_moves:
            if not self.will_hit_food(x):
                prefered_moves.append(x)
                choice = x

        'Avoid dying'
        for x in prefered_moves:
            if not self.will_hit_hazard(x):
                choice = x

        while self.will_hit_hazard(choice):
            choice = random.choice(possible_moves)
        return choice
