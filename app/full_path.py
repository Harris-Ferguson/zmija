from pathfinder_abstract import PathfinderBase
import random

class FullPath(PathfinderBase):
    def next_move(self, target):
        possible_moves = ["up", "down", "left", "right"]
        choice = random.choice(possible_moves)
        pref_list = self.get_pref_moves(self.game.get_self_head(), possible_moves)

        'Pick move in preference order'
        if len(pref_list[0]) > 0:
            return self.pick_best_move(pref_list[0])

        if len(pref_list[1]) > 0:
            return self.pick_best_move(pref_list[1])

        if len(pref_list[2]) > 0:
            return self.pick_best_move(pref_list[2])

        if len(pref_list[3]) > 0:
            return self.pick_best_move(pref_list[3])

        'Avoid dying'
        while self.will_hit_hazard(self.game.get_self_head(), choice):
            choice = random.choice(possible_moves)
        return choice
