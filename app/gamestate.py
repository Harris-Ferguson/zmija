class GameState(object):
    """
    A class to represent the current game state and find game object
    """

    def __init__(self, data):
        self.board = data["board"]
        self.game = data["game"]
        self.me = data["you"]

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

    def find_hazards(self):
        """
        Returns the location of all board hazards
        @return a list of the x-y dicts of locations on the board occupied by hazards
        """
        return self.board["hazards"]

    def get_size(self):
        """
        Returns the dimensions of the gameboard
        @return a dict with the height and width of the game board
        """
        return {"height": self.board["height"], "width":self.board["width"]}

    def find_bad_squares(self):
        """
        Returns all invalid squares (snake or hazard) on the board
        @return a list of x-y dicts of all bad squares on the board
        """
        return self.find_hazards() + self.find_snakes()
