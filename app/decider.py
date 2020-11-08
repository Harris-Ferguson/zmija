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
        possible_moves = ["up", "down", "left", "right"]
        # try to move towards some food
        closest_food = self.game.find_food()
        # if theres no food move in a random direction
        if not closest_food:
            choice = random.choice(possible_moves)
        else:
            choice = self.find_simple_path(closest_food[0])
        # if its dangerous move in a random other direction
        while self.will_hit_hazard(choice):
            choice = random.choice(possible_moves)
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

    def find_closest_food(self):
        pass

    def find_simple_path(self, target):
        """
        simple and janky pathfinder
        Lines up on the x axis first then moves towards the y location
        @param target: and x-y dict of the target square
        @return the next step to take as a string (up, down, left, right)
        """
        current_location = self.game.get_self_head()
        if target["x"] != current_location["x"]:
            if target["x"] < current_location["x"]:
                return "left"
            else:
                return "right"
        elif target["y"] != current_location["y"]:
            if target["y"] < current_location["y"]:
                return "up"
            else:
                return "down"
