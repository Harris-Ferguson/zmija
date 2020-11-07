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

    def get_self_head(self):
        """
        returns the x-y dict of the head of the snake, i.e. returns our current position
        @return the x-y dict of where the snakes head is
        """
        selfsnake = self.me["body"]
        return selfsnake[0]

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
        try:
            return self.board["hazards"]
        except KeyError:
            return []


    def get_board_size(self):
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

    def simulate_move(self, pos, move):
        """
        Returns the new coordinates of a proposed move
        @param pos: the starting coordinates before move
        @param move: A string move (left, right, up, down)
        @return: the new coordinates after a move
        """
        if "right" in move.lower():
            return {"x":pos["x"] + 1, "y": pos["y"]}
        if "left" in move.lower():
            return {"x":pos["x"] - 1, "y": pos["y"]}
        if "up" in move.lower():
            return {"x":pos["x"], "y": pos["y"] + 1}
        if "down" in move.lower():
            return {"x":pos["x"], "y": pos["y"] - 1}
