from pathfinder_abstract import PathfinderBase
import random

class FullPath(PathfinderBase):
    def next_move(self, target):
        choice = random.choice(possible_moves)
        pref_list = self.get_pref_move()

        'Pick move in preference order'
        if len(pref_list[0]) > 0:
            return random.choice(pref_lvl_1)

        if len(pref_list[1]) > 0:
            return random.choice(pref_lvl_2)

        if len(pref_list[2]) > 0:
            return random.choice(pref_lvl_3)

        if len(pref_list[3]) > 0:
            return random.choice(pref_lvl_4)

        'Avoid dying'
        while self.will_hit_hazard(self.game.get_self_head(), choice):
            choice = random.choice(possible_moves)
        return choice
