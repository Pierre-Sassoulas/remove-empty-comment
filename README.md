# remove-empty-comment

Little pre-commit script that remove empty comments from your code

[![PyPI version](https://badge.fury.io/py/remove-empty-comment.svg)](https://badge.fury.io/py/remove-empty-comment)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

> If you feel the need for separators in your code, you might as well start using functions.

## Installation

```yaml
-   repo: https://github.com/Pierre-Sassoulas/remove-empty-comment/
    rev: 1.1.0
    hooks:
    - id: remove-empty-comment
      args: [--meaningless-characters, "-= "]
```

## Use

```
usage: remove-empty-comment [-h] [-c MEANINGLESS_CHARACTERS] [FILES [FILES ...]]

positional arguments:
  FILES                 File names to modify

optional arguments:
  -h, --help            show this help message and exit
  -c MEANINGLESS_CHARACTERS, --meaningless-characters MEANINGLESS_CHARACTERS
                        Characters that have no meaning alone. If there are alone in a comment, it will be removed.
```

## Before

```python
import argparse

###############
# main function
###############
def main():
    """Main function, can you read?

    parameters:
    -----------
    None"""
    a = 1
    b = 2
    c = a + b

    #

    print(c)


# ARGUMENTS
# =========
parser = argparse.ArgumentParser()

# Checking-inputs
# ------------------------------------
print(parser)

```

## After

```python
import argparse

# main function
def main():
    """Main function, can you read?

    parameters:
    -----------
    None"""
    a = 1
    b = 2
    c = a + b


    print(c)


# ARGUMENTS
parser = argparse.ArgumentParser()

# Checking-inputs
print(parser)

```