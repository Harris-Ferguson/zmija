import random
import gamestate
import full_path
import find_path
import minimax

class Decider(object):
    """
    A class to decide the next move
    """

    def __init__(self, data):
        self.game = gamestate.GameState(data)

    def decide(self):
        """
        returns a move choice
        @return a string move choice, either up down left or right
        """
        pathfinder = minimax.MiniMax(self.game)
        return pathfinder.next_move()

    def get_distance(self, coor1, coor2):
        """
        finds the distance between two coordinates
        @return: an integer represents the distance between two given coordinates
        """
        return abs(coor1["x"] - coor2["x"]) + abs(coor1["y"] - coor2["y"])

    def get_closest_food(self, food_list):
        """
        finds the location of the closest food
        @return: a dictionary represents coordinate (x,y) of the closest food to our snake currently on the board
        """
        min_distance = 50
        closest_coor = {}
        for coor in food_list:
            curr_distance = self.get_distance(self.game.get_self_head(), coor)
            if curr_distance < min_distance:
                min_distance = curr_distance
                closest_coor = coor
        return closest_coor

    def get_best_food(self):
        """
        finds the ideal food location to move toward
        @return: a list including a dictionary represents coordinate (x,y) of the most ideal food to our snake currently on the board
        and a boolean value; True if the ideal food is found, False if for every food coordinates, there are other snakes closer.
        """
        # set up variables for loop
        best_coor = self.get_closest_food(gamestate.find_food())
        my_snake_coor = gamestate.get_self_head()
        our_distance_to_food = self.get_distance(my_snake_coor, best_coor)
        bad_coor = False
        curr_food_size = 0

        while curr_food_size + 1 < len(gamestate.find_food()): # stop if there are none food coordinate left to check
            for snake in gamestate.get_remaining_snakes(): # check if other snakes are closer to our ideal food than we are
                if (snake["name"] != "Our Snake Name (temporary)"):  # change the name when we decide our snake's name
                    if self.get_distance(snake["head"], best_coor) < our_distance_to_food:
                        bad_coor = True
                        break

            if bad_coor:    # if they are closer to our current ideal food, pick the next closest food to us in the food list
                curr_food_size += 1    # skip the current food coordinate since it is closer to our opponents
                best_coor = self.get_closest_food(gamestate.find_food()[curr_food_size:])
                our_distance_to_food = self.get_distance(my_snake_coor, best_coor)
            else:
                return [best_coor, True]
        return [best_coor, False]
