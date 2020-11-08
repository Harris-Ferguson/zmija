import pytest
from pathlib import Path
import json
from app.gamestate import *

test_request = json.loads(Path('tests/full_request.json').read_text())
test_game = GameState(test_request)


def test_find_food():
    assert test_game.find_food() == [{"x": 5, "y": 5}, {"x": 9, "y": 0},{"x": 2, "y": 6}]

def test_get_self_head():
    assert test_game.get_self_head() == {"x": 0, "y": 0}

def test_find_snakes():
    assert test_game.find_snakes() ==[{"x": 0, "y": 0},{"x": 1, "y": 0},{"x": 2, "y": 0},{"x": 5, "y": 4},{"x": 5, "y": 3},{"x": 6, "y": 3},{"x": 6, "y": 2}]

def test_find_hazards():
    assert test_game.find_hazards() == [{"x": 0, "y": 0}]

def test_find_bad_squares():
    assert test_game.find_bad_squares() == [{"x": 0, "y": 0},{"x": 0, "y": 0},{"x": 1, "y": 0},{"x": 2, "y": 0},{"x": 5, "y": 4},{"x": 5, "y": 3},{"x": 6, "y": 3},{"x": 6, "y": 2}]

def test_simulate_move():
    assert test_game.simulate_move({"x": 0, "y": 0}, "right") == {"x": 1, "y": 0}
    assert test_game.simulate_move({"x": 0, "y": 0}, "left") == {"x": -1, "y": 0}
    assert test_game.simulate_move({"x": 0, "y": 0}, "up") == {"x": 0, "y": -1}
    assert test_game.simulate_move({"x": 0, "y": 0}, "down") == {"x": 0, "y": 1}
