# __init__.py allows python to treat folder as a package
#python -m pytest test
#tests entire folders

from hello1 import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"

