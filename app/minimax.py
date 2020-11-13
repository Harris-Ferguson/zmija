from pathfinder_abstract import PathfinderBase
from board_simulate import BoardSimulate

class MiniMax(PathfinderBase):
    def next_move(self):
        board = BoardSimulate(self.game.board)
        safe_moves = [x for x in ["right", "left", "up", "down"] if not self.will_hit_hazard(x, self.game.get_self_head())]
        move_values = {}
        for move in safe_moves:
            board.try_move(self.game.get_self(), move)
            move_values[move] = self.minimax(4, board, True)
            board.undo_move()
        return max(move_values, key=move_values.get)

    def heuristic(self, board):
        scalar = 0.0
        if len(self.game.get_self()["body"]) < len(self.get_enemy_snake()["body"]):
            scalar -= 0.2
        if len(self.game.get_self()["body"]) > len(self.get_enemy_snake()["body"]):
            scalar += 0.2
        return scalar


    def minimax(self, depth, board, max_player):
        if depth == 0 or len(board.board["snakes"]) <= 1:
            return self.heuristic(board)
        if max_player:
            value = -1.0
            for move in ["right", "left", "up", "down"]:
                board.try_move(self.get_maxing_snake(), move)
                attempt = self.minimax(depth - 1, board, False)
                value = max(value, attempt)
                board.undo_move()
            return value
        else:
            value = 1.0
            for move in ["right", "left", "up", "down"]:
                enemy_snake = self.get_enemy_snake()
                board.try_move(enemy_snake, move)
                attempt = self.minimax(depth - 1, board, True)
                value = max(value, attempt)
                board.undo_move()
            return value

    def get_enemy_snake(self):
        enemy_snake = {}
        for snake in self.game.board["snakes"]:
            if snake["name"] != self.game.get_self()["name"]:
                enemy_snake = snake
        return enemy_snake

    def get_maxing_snake(self):
        max_snake = {}
        for snake in self.game.board["snakes"]:
            if snake["name"] == self.game.get_self()["name"]:
                max_snake = snake
        return max_snake