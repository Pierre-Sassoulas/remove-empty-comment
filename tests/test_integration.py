from pathlib import Path
from unittest.mock import patch

import pytest

from remove_empty_comment.__main__ import main, transform


def test_integration():
    with patch("sys.argv", ["remove-empty-comment"]):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.value.code == 0
    with patch("sys.argv", ["remove-empty-comment", __file__, "-c", "#, -"]):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.value.code == 0


def test_transform():
    fixture_file = str(Path(__file__).parent / "fixture.py")
    with open(fixture_file) as f:
        content = f.readlines()
    new_content = transform(content, meaningless_characters=["#"])
    assert new_content == [
        "import argparse\n",
        "\n",
        "# main function\n",
        "def main():\n",
        '    """Main function, can you read?\n',
        "\n",
        "    parameters:\n",
        "    -----------\n",
        '    None"""\n',
        "    a = 1\n",
        "    b = 2\n",
        "    c = a + b\n",
        "\n",
        "\n",
        "    print(c)\n",
        "\n",
        "\n",
        "# ARGUMENTS\n",
        "# =========\n",
        "parser = argparse.ArgumentParser()\n",
        "\n",
        "# Checking-inputs\n",
        "# ------------------------------------\n",
        "print(parser)\n",
    ]
    new_content = transform(content, meaningless_characters=["#", "-", "=", " "])
    assert new_content == [
        "import argparse\n",
        "\n",
        "# main function\n",
        "def main():\n",
        '    """Main function, can you read?\n',
        "\n",
        "    parameters:\n",
        "    -----------\n",
        '    None"""\n',
        "    a = 1\n",
        "    b = 2\n",
        "    c = a + b\n",
        "\n",
        "\n",
        "    print(c)\n",
        "\n",
        "\n",
        "# ARGUMENTS\n",
        "parser = argparse.ArgumentParser()\n",
        "\n",
        "# Checking-inputs\n",
        "print(parser)\n",
    ]
