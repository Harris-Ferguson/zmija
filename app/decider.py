import random

import gamestate

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
        # TODO: This is currently just picking a random move.
        possible_moves = ["up", "down", "left", "right"]
        choice = random.choice(possible_moves)
        while self.will_hit_hazard(choice):
            choice = random.choice(possible_moves)
        print(choice)
        return choice


    def will_hit_hazard(self, move):
        """
        Takes the proposed move and checks if it will hit a hazard on the board
        @param a move choice string (up, down, right, left)
        @return True if the move will hit a hazard, false if the move is safe
        """
        bad_squares = self.game.find_bad_squares()
        new_location = self.game.simulate_move(self.game.get_self_head(), move)
        # Check if we will hit a wall
        if new_location["x"] > self.game.get_board_size()["width"] or new_location["y"] > self.game.get_board_size()["height"] or new_location["x"] < 0 or new_location["y"] < 0:
            return True
        # check if we will hit a bad square
        for square in bad_squares:
            if new_location["x"] == square["x"] and new_location["y"] == square["y"]:
                return True
        return False
