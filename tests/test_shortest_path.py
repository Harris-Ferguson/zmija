import pytest
from pathlib import Path
import json
from app.shortest_path import *
from app.gamestate import *
import collections

test_request = json.loads(Path('tests/small_test_board.json').read_text())
test_game = GameState(test_request)
test_pathfinder = ShortestPath(test_game)

"""
Visual of this test board:
S - our snake
A - another snake
F - Food

*  0 1 2 3 4
0  F S S A
1        A
2
3          F
4          F
"""

def test_get_safe_squares():
    expected_squares = [
    {"x":0,"y":0},{"x":0,"y":1},{"x":0,"y":2},{"x":0,"y":3},{"x":0,"y":4},
    {"x":1,"y":1},{"x":1,"y":2},{"x":1,"y":3},{"x":1,"y":4},
    {"x":2,"y":1},{"x":2,"y":2},{"x":2,"y":3},{"x":2,"y":4},
    {"x":3,"y":2},{"x":3,"y":4},
    {"x":4,"y":0},{"x":4,"y":1},{"x":4,"y":2},{"x":4,"y":3},{"x":4,"y":4}]
    assert equal_ignore_order(test_pathfinder.get_safe_squares(), expected_squares)

def equal_ignore_order(a, b):
    """Helper function to check if two collections are equal regardless of order"""
    for item in a:
        try:
            i = b.index(item)
        except ValueError:
            return False
        b = b[:i] + b[i+1:]
    return not b
