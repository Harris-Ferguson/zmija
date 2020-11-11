import pytest
from pathlib import Path
import json
from app.decider import *

test_request = json.loads(Path('tests/small_test_board.json').read_text())
test_decider = Decider(test_request)
