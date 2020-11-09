from abc import abstractmethod

class PathfinderBase(object):

    def __init__(self, gamestate):
        """
        Constructor
        @param gamestate: GameState object of the current game
        """
        self.game = gamestate
        self.path = []
        super().__init__()

    @abstractmethod
    def next_move(start):
        """
        Abstract path finding method
        @param start: the starting point
        @param end: the end point
        @return: the move
        """
        pass

    def is_off_edge(self, point):
        """
        Checks if a given point is off the game board
        @param point: an xy dict point
        @return: true if the point is on the board, false otherwise
        """
        print(point)
        if point["x"] > self.game.get_board_size()["width"] or point["x"] < 0:
            return True
        if point["y"] > self.game.get_board_size()["height"] or point["y"] < 0:
            return True
        return False


    def will_hit_hazard(self, move):
        """
        Takes the proposed move and checks if it will hit a hazard on the board
        @param a move choice string (up, down, right, left)
        @return True if the move will hit a hazard, false if the move is safe
        """
        bad_squares = self.game.find_bad_squares()
        new_location = self.simulate_move(self.game.get_self_head(), move)
        # Check if we will hit a wall
        if self.is_off_edge(new_location):
            return True
        # check if we will hit a bad square
        for square in bad_squares:
            if new_location["x"] == square["x"] and new_location["y"] == square["y"]:
                return True
        return False

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
            return {"x":pos["x"], "y": pos["y"] - 1}
        if "down" in move.lower():
            return {"x":pos["x"], "y": pos["y"] + 1}

    def find_closest_food(self):
        pass
