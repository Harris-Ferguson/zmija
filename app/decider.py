import random
import gamestate
import simple_path
import full_path

class Decider(object):
    """
    An class to decide the next move
    """

    def __init__(self, data):
        self.game = gamestate.GameState(data)

    def decide(self):
        """
        returns a move choice
        @return a string move choice, either up down left or right
        """
        pathfinder = simple_path.SimplePath(self.game)
        return pathfinder.next_move()
