import game

class Decider(object):
    """
    An class to decide the next move
    """

    def __init__(self, gameboard, game):
        self.game = Finder(gameboard, game)
