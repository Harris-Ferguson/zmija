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
    def next_move(self, target):
        """
        Abstract path finding method
        @param target: where we are trying to get
        @return: the move
        """
        pass

    def is_off_edge(self, point):
        """
        Checks if a given point is off the game board
        @param point: an xy dict point
        @return: true if the point is on the board, false otherwise
        """
        if point["x"] > self.game.get_board_size()["width"] - 1 or point["x"] < 0:
            return True
        if point["y"] > self.game.get_board_size()["height"] - 1 or point["y"] < 0:
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

    def square_on_edge(self, coord):
        """
        Check if a square is on the edge of the board
        :param coord: xy dictionary of the spot on the board to check
        """
        if coord["x"] == self.game.get_board_size()["width"] - 1 or coord["y"] == self.game.get_board_size()[
            "height"] - 1:
            return True
        if coord["x"] == 0 or coord["y"] == 0:
            return True
        return False

    def will_trap_self(self, move):
        """
        Check if a move leads to trapping ourselves
        currently just checks in a straight line
        :param coord: a string move (left, right, up, down)
        """
        # this is a gross function. idk why i wrote it like this
        current_spot = self.game.get_self_head()
        next_spot = self.simulate_move(current_spot, move)
        snake = self.game.get_self()["body"]

        # Checks if we are trapping ourselves against a wall by turning into ourself
        if current_spot["x"] > next_spot["x"]:
            for spot in snake:
                if next_spot["x"] < spot["x"]:
                    return True
        if current_spot["x"] < next_spot["x"]:
            for spot in snake:
                if next_spot["x"] > spot["x"]:
                    return True
        if current_spot["y"] > next_spot["y"]:
            for spot in snake:
                if next_spot["y"] < spot["y"]:
                    return True
        if current_spot["y"] < next_spot["y"]:
            for spot in snake:
                if next_spot["y"] > spot["y"]:
                    return True

    def will_hit_food(self, move):
        """
        Takes the proposed move and checks if it will it a food on the board
        :param move: a move choice string (up, down, right, left)
        :return: True if the move will hit a food, false if the move does not.
        """

        food_spots = self.game.find_food()
        new_location = self.simulate_move(self.game.get_self_head(), move)
        # Check if we hit a food
        for food in food_spots:
            if new_location["x"] == food["x"] and new_location["y"] == food["y"]:
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
            return {"x": pos["x"] + 1, "y": pos["y"]}
        if "left" in move.lower():
            return {"x": pos["x"] - 1, "y": pos["y"]}
        if "down" in move.lower():
            return {"x": pos["x"], "y": pos["y"] - 1}
        if "up" in move.lower():
            return {"x": pos["x"], "y": pos["y"] + 1}

    def find_closest_food(self):
        pass

    def head_collision_chance(self, move):
        """
        Checks if the move is in danger of a head to head collision
        with another snake.
        :param move:  A string move (left, right, up, down)
        :return: True if there is a chance for a head collision, false if there is no chance.
        """
        heads = self.game.find_other_snake_heads()
        new_location = self.simulate_move(self.game.get_self_head(), move)
        possible_enemy_moves = ["up", "right", "left", "down"]

        for head in heads:
            for move in possible_enemy_moves:
                new_enemy_move = self.simulate_move(head, move)
                if new_enemy_move["x"] == new_location["x"] and new_enemy_move["y"] == new_location["y"]:
                    return True
        return False
