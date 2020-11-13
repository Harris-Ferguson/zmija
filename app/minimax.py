from pathfinder_abstract import PathfinderBase
from board_simulate import BoardSimulate

class MiniMax(PathfinderBase):
    def __init__(self, game):
        super().__init__(game)
        self.simBoard = BoardSimulate(self.game.board)
        
    def next_move(self):
        safe_moves = [x for x in ["right", "left", "up", "down"] if not self.will_hit_hazard(x, self.game.get_self_head())]
        move_values = {}
        for move in safe_moves:
            self.simBoard.try_move(self.game.get_self(), move)
            move_values[move] = self.minimax(5, True)
            self.simBoard.undo_move()
        return max(move_values, key=move_values.get)

    def heuristic(self):
        """
        Heuristic function
        :param self.simBoard: the self.simBoard simulation state to check the Heuristic function on (self.simBoardSimulate Object)
        :return: float scalar value of how good this node is for the maxing player
        """
        scalar = 0.0
        if self.get_maxing_snake()['body'][0]['x'] == self.simBoard.board["width"] - 1 or self.get_maxing_snake()['body'][0]['y'] \
                == self.simBoard.board["height"] - 1:
            scalar -= 0.4
        if self.get_maxing_snake()['body'][0]['x'] == 0 or self.get_maxing_snake()['body'][0]['y'] == 0:
            scalar -= 0.4
        if self.is_close_to_food():
            scalar += 0.3
        return scalar

    def is_close_to_food(self):
        self_head = self.get_maxing_snake()["body"][0]
        for food in self.simBoard.board["food"]:
            if abs(food["x"] - self_head["x"]) + abs(food["x"] - self_head["x"]) <= 3:
                return True
        return False

    def is_terminal_leaf(self):
        """
        checks if the board state is a terminal leaf of our minmax tree (i.e. we died)
        :return: True if this state is a terminal leaf
        """
        if len(self.simBoard.board["snakes"]) <= 1:
            return True
        for move in ["left", "right", "up", "down"]:
            if self.will_hit_hazard(move, self.get_maxing_snake()["body"][0]):
                return True
        if self.is_off_edge(self.get_maxing_snake()["body"][0]):
            return True
        return False


    def minimax(self, depth, max_player):
        """
        Minimax implementation
        :param depth: Depth to search through the tree
        :max_player: is this the maxing player or not?
        :return: node edge value of the optimal node (move)
        """
        if depth == 0 or self.is_terminal_leaf():
            return self.heuristic()
        if max_player:
            value = -1.0
            for move in ["right", "left", "up", "down"]:
                self.simBoard.try_move(self.get_maxing_snake(), move)
                attempt = self.minimax(depth - 1, False)
                value = max(value, attempt)
                self.simBoard.undo_move()
            return value
        else:
            value = 1.0
            for move in ["right", "left", "up", "down"]:
                enemy_snake = self.get_enemy_snake()
                self.simBoard.try_move(enemy_snake, move)
                attempt = self.minimax(depth - 1, True)
                value = max(value, attempt)
                self.simBoard.undo_move()
            return value

    def get_enemy_snake(self):
        """
        Returns the opponent snake 
        """
        enemy_snake = {}
        for snake in self.simBoard.board["snakes"]:
            if snake["name"] != self.game.get_self()["name"]:
                enemy_snake = snake
        return enemy_snake

    def get_maxing_snake(self):
        max_snake = {}
        for snake in self.simBoard.board["snakes"]:
            if snake["name"] == self.game.get_self()["name"]:
                max_snake = snake
        return max_snake

    def is_off_edge(self, point):
        """
        Checks if a given point is off the game board
        @param point: an xy dict point
        @return: true if the point is on the board, false otherwise
        """
        if point["x"] > self.simBoard.board["width"] - 1 or point["x"] < 0:
            return True
        if point["y"] > self.simBoard.board["height"] - 1 or point["y"] < 0:
            return True