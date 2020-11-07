import random

import gamestate

class Decider(object):
    """
    An class to decide the next move
    """

    def __init__(self, gameboard, game):
        self.gamestate = gamestate.GameState(gameboard, game)

    def decide(self):
        """
        returns a move choice
        @return a string move choice, either up down left or right
        """
        # TODO: This is currently just picking a random move.
        possible_moves = ["up", "down", "left", "right"]
        return random.choice(possible_moves)
