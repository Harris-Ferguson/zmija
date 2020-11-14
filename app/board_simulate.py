from pathfinder_abstract import PathfinderBase

class BoardSimulate(object):
    def __init__(self, board):
        self.board = board
        self.last_board = self.board

    # note to self: run this function once per snake on the board and you essentially have
    # game engine. this was written by refrencing the official game rules at:
    # https://docs.battlesnake.com/references/rules
    # might be a good side project...
    def make_moves(self, requests):
        """
        :param request: list of dicts:
            "name"
            "move"
        """
        self.last_board = self.board
        for request in requests:
            #self.board["snakes"][request["name"]]
            next_move = PathfinderBase.simulate_move(self.board["snakes"][request["name"]]["body"][0], request["move"])
            self.board["snakes"][request["name"]]["body"].insert(0, next_move)
            self.board["snakes"][request["name"]]["body"].remove(self.board["snakes"][request["name"]]["body"][-1])
            self.board["snakes"][request["name"]]["health"] -= 1

            #consume food
            for food in self.board["food"]:
                if food == next_move:
                    self.board["snakes"][request["name"]]["health"] == 100
                    self.board["snakes"][request["name"]]["body"].append(self.board["snakes"][request["name"]]["body"][-1])
                    self.board["food"].remove(food)

            #food spawn not simulated

        #check for deaths!
        for snake in self.board["snakes"]:
            if snake["health"] == 0:
                self.board["snakes"].remove(snake)
            if self.out_of_bounds(snake):
                self.board["snakes"].remove(snake)
            if snake["body"][0] in snake["body"]:
                self.board["snakes"].remove(snake)
            for other in self.board["snakes"]:
                if other != snake:
                    if snake["body"][0] in other["body"][1:]:
                        self.board["snakes"].remove(snake)
                    if snake["body"][0] == other["body"][0]:
                        if len(snake["body"]) == len(other["body"]):
                            self.board["snakes"].remove(snake)
                            self.board["snakes"].remove(other)
                        elif len(snake["body"]) > len(other["body"]):
                            self.board["snakes"].remove(snake)
                        else:
                            self.board["snakes"].remove(other)

    def out_of_bounds(snake):
        if snake["body"][0]["x"] >= self.board["width"] or snake["body"][0]["y"] >= self.board["height"] or snake["body"][0]["x"] < 0 or snake["body"][0]["y"] < 0:
            return True

    def undo_move(self):
        self.board = self.last_board


    def create_invalid_squares(self):
        """
        creates a list of every square which causes death
        """
        bad_squares = []
        for snake in self.board["snakes"]:
            for spot in snake["body"]:
                # get every square that isn't a tail
                if spot != snake["body"][-1]:
                    bad_squares.append(spot)
        for x in range(0, self.board["width"] - 1):
            for y in range(0, self.board['height'] - 1):
                bad_squares.append({"x": x, "y": self.board["height"]})
                bad_squares.append({"x": x, "y": -1})
                bad_squares.append({"x": self.board["width"], "y": y})
                bad_squares.append({"x": -1, "y": y})
        return bad_squares
