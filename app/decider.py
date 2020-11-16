import random
import gamestate
import simple_path
import full_path
import find_path

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
        food = self.get_best_food()
        if not food[1]:
          pathfinder = full_path.FullPath(self.game)
        elif self.shortest_snake():
          pathfinder = find_path.FindPath(self.game)
        else:
          pathfinder = find_path.FindPath(self.game)
        print(type(pathfinder))
        return pathfinder.next_move(food[0])

    def shortest_snake(self):
    """
    Checks if we are the shortest snake
    :return: true if we are the shorest snake on the board, false otherwise
    """
      for snake in self.game.get_other_snakes():
        if len(self.game.get_self()["body"]) < len(snake["body"]):
          return True
      return False

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
        best_coor = self.get_closest_food(self.game.find_food())
        if not best_coor:  # if there is no food on the board
            return [best_coor, False]
        my_snake_coor = self.game.get_self_head()
        our_distance_to_food = self.get_distance(my_snake_coor, best_coor)
        bad_coor = False
        curr_food_size = 0

        # If there is only one food on the board
        if len(self.game.find_food()) == 1:
            for snake in self.game.get_remaining_snakes():  # check if other snakes are closer to our ideal food than we are
                if (snake["name"] != self.game.get_self()["name"]):
                    if self.get_distance(snake["head"], best_coor) <= our_distance_to_food:
                        bad_coor = True
                        break
            if bad_coor:
                return [best_coor, False]  # if the food on the board is not worth getting

        # If there is more than one one food on the board
        while curr_food_size + 1 < len(self.game.find_food()): # stop if there is no food coordinate left to check
            for snake in self.game.get_remaining_snakes(): # check if other snakes are closer to our ideal food than we are
                if (snake["name"] != self.game.get_self()["name"]):
                    if self.get_distance(snake["head"], best_coor) <= our_distance_to_food:
                        bad_coor = True
                        break
            if bad_coor:    # if they are closer to our current ideal food, pick the next closest food to us in the food list
                curr_food_size += 1    # skip the current food coordinate since it is closer to our opponents
                best_coor = self.get_closest_food(self.game.find_food()[curr_food_size:])
                our_distance_to_food = self.get_distance(my_snake_coor, best_coor)
            else:
                return [best_coor, True] # if a good food is found on the board
        return [best_coor, False]  # if the food on the board is not worth getting
