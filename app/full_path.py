from pathfinder_abstract import PathfinderBase
import random


class FullPath(PathfinderBase):
    def next_move(self):
        possible_moves = ["up", "down", "left", "right"]
        pref_lvl_1 = []
        pref_lvl_2 = []
        food = self.game.find_food()
        choice = random.choice(possible_moves)

        'Avoid any food and trapping self'
        for x in possible_moves:
            if not self.will_hit_food(x) and not self.will_hit_hazard(x):
                pref_lvl_1.append(x)
            elif self.will_hit_food(x) and not self.will_hit_hazard(x):
                pref_lvl_2.append(x)

        'Pick move in preference order'
        if len(pref_lvl_1) > 0:
            return random.choice(pref_lvl_1)

        if len(pref_lvl_2) > 0:
            return random.choice(pref_lvl_2)

        'Avoid dying'
        while self.will_hit_hazard(choice):
            choice = random.choice(possible_moves)
        return choice
