from pathlib import Path
from unittest.mock import patch

import pytest

from remove_empty_comment.__main__ import main, transform


def test_integration():
    with patch("sys.argv", ["remove-empty-comment"]):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.value.code == 0


def test_transform():
    fixture_file = str(Path(__file__).parent / "fixture.py")
    with open(fixture_file) as f:
        content = f.readlines()
    new_content = transform(content)
    assert new_content == [
        "# main function\n",
        "def main():\n",
        "    a = 1\n",
        "    b = 2\n",
        "    c = a + b\n",
        "    print(c)\n"
    ]
