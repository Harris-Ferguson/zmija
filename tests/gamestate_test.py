import pytest
from pathlib import Path
import json

from app.gamestate import *

test_request = json.loads(Path('tests/full_request.json').read_text())
test_game = GameState(test_request)


def test_find_food():
    assert test_game.find_food() == [{"x": 5, "y": 5}, {"x": 9, "y": 0},{"x": 2, "y": 6}]
