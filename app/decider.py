import random

import gamestate

class Decider(object):
    """
    An class to decide the next move
    """

    def __init__(self, data):
        self.gamestate = gamestate.GameState(data)

    def decide(self):
        """
        returns a move choice
        @return a string move choice, either up down left or right
        """
        # TODO: This is currently just picking a random move.
        possible_moves = ["up", "down", "left", "right"]
        return random.choice(possible_moves)

    def will_hit_hazard(move):
        """
        Takes the proposed move and checks if it will hit a hazard on the board
        @param a move choice string (up, down, right, left)
        @return True if the move will hit a hazard, false if the move is safe
        """
        bad_squares = gamestate.find_bad_squares()
        new_location = gamestate.simulate_move(gamestate.me["body"][0], move)
        for square in bad_squares:
            if new_location["x"] == square["x"] and new_location["y"] == square["y"]:
                return False
        return True
