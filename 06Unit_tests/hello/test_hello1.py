from hello1 import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("me") == "hello, me"

#run python -m pytest test_hello1.py 