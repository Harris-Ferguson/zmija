import random
import gamestate
import simple_path
import full_path
import find_path

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
        pathfinder = find_path.FindPath(self.game)
        closest_food = self.game.find_food()
        if not closest_food:
            choice = pathfinder.find_path({"x":0,"y":0})
        else:
            choice = pathfinder.find_path(closest_food[0])
        return choice
