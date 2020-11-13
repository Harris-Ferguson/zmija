from pathfinder_abstract import PathfinderBase
import random


class FullPath(PathfinderBase):
    def next_move(self, target):
        possible_moves = ["up", "down", "left", "right"]
        pref_lvl_1 = []
        pref_lvl_2 = []
        pref_lvl_3 = []
        pref_lvl_4 = []
        food = self.game.find_food()
        choice = random.choice(possible_moves)

        'Avoid any food and trapping self'
        for x in possible_moves:
            if not self.will_hit_food(x) and not self.will_hit_hazard(x, self.game.get_self_head()) and not self.head_collision_chance(x):
                pref_lvl_1.append(x)
            elif self.will_hit_food(x) and not self.will_hit_hazard(x, self.game.get_self_head()) and not self.head_collision_chance(x):
                pref_lvl_2.append(x)
            elif not self.will_hit_food(x) and not self.will_hit_hazard(x, self.game.get_self_head()) and self.head_collision_chance(x):
                pref_lvl_3.append(x)
            elif self.will_hit_food(x) and not self.will_hit_hazard(x, self.game.get_self_head()) and self.head_collision_chance(x):
                pref_lvl_4.append(x)

        'Pick move in preference order'
        if len(pref_lvl_1) > 0:
            return random.choice(pref_lvl_1)

        if len(pref_lvl_2) > 0:
            return random.choice(pref_lvl_2)

        if len(pref_lvl_3) > 0:
            return random.choice(pref_lvl_3)

        if len(pref_lvl_4) > 0:
            return random.choice(pref_lvl_4)

        'Avoid dying'
        while self.will_hit_hazard(choice, self.game.get_self_head()):
            choice = random.choice(possible_moves)
        return choice
