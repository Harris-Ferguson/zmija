class Finder(object):
    """
    An object to process the game state and find the location of various game objects such as
    food and snakes
    """

    def __init__(self, gameboard, game):
        self.board = gameboard
        self.game = game

    def find_food(self):
        """
        returns the location of all the food on the board
        @return a list of dict of the x-y locations of the food
        """
        return self.board["food"]

    def find_snakes(self):
        """
        Returns the location of all squares occupied by snakes (including self)
        @return a list of x-y dicts of locations on the board occupied by snakes
        """
        snakes = self.board["snakes"]
        occupied = []
        for snake in snakes:
            for spot in snake["body"]:
                occupied.append(spot)
        return occupied
