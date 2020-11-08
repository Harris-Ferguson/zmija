import pytest
from pathlib import Path
import json
from app.decider import *

test_request = json.loads(Path('tests/small_test_board.json').read_text())
test_decider = Decider(test_request)

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

def test_closest_food():
    assert test_decider.find_closest_food() == {"x": 0, "y": 0}

def test_will_hit_hazard():
    # in the test position from small_test_board, down is the only valid move
    assert test_decider.will_hit_hazard("down") == False
    assert test_decider.will_hit_hazard("up") == True
    assert test_decider.will_hit_hazard("right") == True
    assert test_decider.will_hit_hazard("left") == True
