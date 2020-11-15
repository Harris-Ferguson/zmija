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

    def get_self(self):
        """
        Returns the current snake
        """
        return self.me

    def get_self_head(self):
        """
        returns the x-y dict of the head of the snake, i.e. returns our current position
        @return the x-y dict of where the snakes head is
        """
        selfsnake = self.me["body"]
        return selfsnake[0]

    def get_remaining_snakes(self):
        """
        returns the remaining snakes on the board (including our snake)
        @return the remaining snakes currently on the board (1-4)
        """
        return self.board["snakes"]

    def get_other_snakes(self):
        """
        returns the remaining snakes on the board (excluding our snake)
        @return the remaining snakes currently on the board (1-3)
        """
        snakes = []
        for snake in self.board["snakes"]:
            if snake["name"] != self.get_self()["name"]:
                snakes.append(snake)
        return snakes

    def get_health(self):
        """
        returns the health of our snake
        :return: an integer represents the health level of our snake
        """
        return self.me["health"]

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
        return {"height": self.board["height"], "width": self.board["width"]}

    def find_bad_squares(self):
        """
        Returns all invalid squares (snake or hazard) on the board
        @return a list of x-y dicts of all bad squares on the board
        """
        return self.find_hazards() + self.find_snakes()

    def find_other_snake_heads(self):
        """
        Find and return info on all of the other snakes head positions.
        :return: A list of dicts holding coordinates of snake heads(including self)
        """
        heads = []
        for snake in self.get_remaining_snakes():
            # first element is the head
            heads.append(snake["body"][0])
        heads.remove(self.get_self_head())
        return heads

    def identify_snake(self, position):
        """
        Find the snake whose body is on the given position (x-y)
        :param position: x-y dictionary represents coordinate of a snake on the board to identify
        :return: a dictionary represents the snake if there is a snake at the given position;
        returns an empty dictionary otherwise
        """
        for snake in self.get_remaining_snakes():
            for coordinate in snake["body"]:
                if coordinate["x"] == position["x"] and coordinate["y"] == position["y"]:
                    return snake
        return {}
