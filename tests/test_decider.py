import pytest
from pathlib import Path
import json

from app.decider import *

test_request = json.loads(Path('tests/full_request.json').read_text())
test_decider = Decider(test_request)

def test_closest_food():
    assert test_decider.find_closest_food() == {"x": 1, "y": 2}
