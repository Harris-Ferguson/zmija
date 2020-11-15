from abc import abstractmethod
import random

class PathfinderBase(object):

    def __init__(self, gamestate):
        """
        Constructor
        @param gamestate: GameState object of the current game
        """
        self.game = gamestate
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

    def will_hit_hazard(self, snake_head, move):
        """
        Takes the proposed move and checks if it will hit a hazard on the board
        @param snake_head a dictionary represents the coordinate of the head of the snake to check
        @param a move choice string (up, down, right, left)
        @return True if the move will hit a hazard, false if the move is safe
        """
        bad_squares = self.game.find_bad_squares()
        new_location = self.simulate_move(snake_head, move)
        # Check if we will hit a wall
        if self.is_off_edge(new_location):
            return True
        # Ignore the tail of our snake
        if new_location["x"] == self.game.get_self()["body"][-1]["x"] and new_location["y"] == \
                self.game.get_self()["body"][-1]["y"]:
            return False
        # Ignore the tails of other snakes if they are not about to eat something
        other_snakes = self.game.get_other_snakes()
        for snake in other_snakes:
            if new_location["x"] == snake["body"][-1]["x"] and new_location["y"] == snake["body"][-1]["y"]:
                # if the snake whose tail we are about to cross is not near any food then we are safe; we are in danger otherwise
                if self.will_hit_food(snake_head, "left") or self.will_hit_food(snake_head, "right") or self.will_hit_food(
                        snake_head, "up") or self.will_hit_food(snake_head, "down"):
                    return True
                else:
                    return False
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

    def will_hit_food(self, snake_head, move):
        """
        Takes the proposed move and checks if it will it a food on the board
        :param move: a move choice string (up, down, right, left)
        :param snake_head: a dictionary represents the coordinate of the head of the snake to check
        :return: True if the move will hit a food, false if the move does not.
        """
        food_spots = self.game.find_food()
        new_location = self.simulate_move(snake_head, move)
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

    def head_collision_chance(self, snake_head, move):
        """
        Checks if the move is in danger of a head to head collision
        with another snake.
        :param move:  A string move (left, right, up, down)
        :param snake_head: a dictionary represents the coordinate of the head of the snake to check
        :return: True if there is a chance for a head collision, false if there is no chance.
        """
        heads = self.game.find_other_snake_heads()
        new_location = self.simulate_move(snake_head, move)
        possible_enemy_moves = ["up", "right", "left", "down"]

        for head in heads:
            for move in possible_enemy_moves:
                new_enemy_move = self.simulate_move(head, move)
                if new_enemy_move["x"] == new_location["x"] and new_enemy_move["y"] == new_location["y"]:
                    return True
        return False

    def get_pref_moves(self, snake_head, possible_moves):
        """
        This function finds the best possible moves our snake can have and categorize them in 4 preference levels
        :param snake_head: a dictionary represents the coordinate of the head of the snake to check
        :param possible_moves: a list of possible moves
        :return: A list of 4 lists with each list contain a move(s); list at index 0 has preference level of 1,
        list at index 1 has preference level of 2,...
        """
        pref_lvl_1 = []
        pref_lvl_2 = []
        pref_lvl_3 = []
        pref_lvl_4 = []

        'Avoid any food and trapping self'
        for x in possible_moves:
            # if no food and no head collision chance
            if not self.will_hit_food(snake_head, x) and not self.will_hit_hazard(
                    snake_head, x) and not self.head_collision_chance(snake_head, x):
                pref_lvl_1.append(x)
            # if food and no head collision chance
            elif self.will_hit_food(snake_head, x) and not self.will_hit_hazard(
                    snake_head, x) and not self.head_collision_chance(snake_head, x):
                pref_lvl_2.append(x)
            # if no food and collision chance
            elif not self.will_hit_food(snake_head, x) and not self.will_hit_hazard(
                    snake_head, x) and self.head_collision_chance(snake_head, x):
                pref_lvl_3.append(x)
            # if food and head collision chance
            elif self.will_hit_food(snake_head, x) and not self.will_hit_hazard(
                    snake_head, x) and self.head_collision_chance(snake_head, x):
                pref_lvl_4.append(x)
        return [pref_lvl_1, pref_lvl_2, pref_lvl_3, pref_lvl_4]

    def pick_best_move(self, pref_level):
        """
        Returns the best move out of all the available moves in a preference level
        :param pref_level: a list representing a preference level containing moves that the snake can choose from
        :return: a string represents the best move that the snake should take (right, left, up, down)
        """
        possible_moves = ["up", "down", "left", "right"]
        best_move = random.choice(possible_moves)  # this is the move without the most freedom, least hazard around it
        min_hazard = 4  # the least number of hazard to compare
        for move in pref_level:
            pref_list_second = self.get_pref_moves(self.simulate_move(self.game.get_self_head(), move), possible_moves)
            num_of_hazard = 4 - (len(pref_list_second[0]) + len(pref_list_second[1]) + len(pref_list_second[2]) + len(
                pref_list_second[3]))
            if num_of_hazard < min_hazard:
                best_move = move
                min_hazard = num_of_hazard
        return best_move

    def trap_lookahead(self, move, depth):
      """
      Looks fowards a few moves to see if we will get trapped
      """
      if depth == 0:
        return False
      if self.square_on_hazard(pos):
        return True
      next_spot = self.simulate_move(pos, move)
      if self.trap_lookahead(next_spot, move, depth - 1):
          return True
    
    def square_on_hazard(self, pos):
      bad_squares = self.game.find_bad_squares()
      for square in bad_squares:
        if pos == square:
          return True
      return False