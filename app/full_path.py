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
            # if no food and no head collision chance
            if not self.will_hit_food(self.game.get_self(), x) and not self.will_hit_hazard(x) and not self.head_collision_chance(x):
                pref_lvl_1.append(x)
            # if food and no head collision chance
            elif self.will_hit_food(self.game.get_self(), x) and not self.will_hit_hazard(x) and not self.head_collision_chance(x):
                pref_lvl_2.append(x)
            # if no food and collision chance
            elif not self.will_hit_food(self.game.get_self(), x) and not self.will_hit_hazard(x) and self.head_collision_chance(x):
                pref_lvl_3.append(x)
            # if food and head collision chance
            elif self.will_hit_food(self.game.get_self(), x) and not self.will_hit_hazard(x) and self.head_collision_chance(x):
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
        while self.will_hit_hazard(choice):
            choice = random.choice(possible_moves)
        return choice
